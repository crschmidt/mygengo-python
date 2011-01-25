#!/usr/bin/python

"""
	PyGengo is an unofficial Python library for interfacing with the myGengo API.
	It's released under the LGPL and totally, freely available. Check it out on Github
	if you find any issues!

	Questions, comments? ryan@venodesigns.net
"""

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.0.0'

import httplib2
import mimetypes
import mimetools
import re
import hmac

from hashlib import sha1
from urllib import urlencode
from time import time
from operator import itemgetter

# pygengo_mockdb is a file with a dictionary of every API endpoint for myGengo.
from mockdb import api_urls, apihash
from error_codes import errors

# There are some special setups (like, oh, a Django application) where
# simplejson exists behind the scenes anyway. Past Python 2.6, this should
# never really cause any problems to begin with.
try:
	# Python 2.6 and up
	import json
except ImportError:
	try:
		# Python 2.6 and below (2.4/2.5, 2.3 is not guranteed to work with this library to begin with)
		import simplejson as json
	except ImportError:
		try:
			# This case gets rarer by the day, but if we need to, we can pull it from Django provided it's there.
			from django.utils import simplejson as json
		except:
			# Seriously wtf is wrong with you if you get this Exception.
			raise Exception("PyGengo requires the simplejson library (or Python 2.6+) to work. http://www.undefined.org/python/")

class PyGengoError(Exception):
	"""
		Generic error class, catch-all for most PyGengo issues.
		Special cases are handled by APILimit and AuthError.

		Note: You need to explicitly import them into your code, e.g:

		from pygengo import PyGengoError, APILimitError, AuthError
	"""
	def __init__(self, msg, error_code=None):
		self.msg = msg
		if error_code == 1000:
			# Auth errors tend to be the most requested for their own
			# Exception instances, so give it to the masses, yo.
			raise PyGengoAuthError(msg)
	
	def __str__(self):
		return repr(self.msg)


class PyGengoAuthError(PyGengoError):
	"""
		Raised when you try to access a protected resource and it fails due to some issue with
		your authentication.
	"""
	def __init__(self, msg):
		self.msg = msg
	
	def __str__(self):
		return repr(self.msg)


class PyGengo(object):
	def __init__(self, public_key = None, private_key = None, sandbox = False, api_version = 1, headers = None):
		"""PyGengo(public_key = None, private_key = None, sandbox = False, headers = None)

			Instantiates an instance of PyGengo. While you can have multiple instances of PyGengo going at once, this is not recommended
			practice, and this library will never be held responsible for anything myGengo may do to you if you decide to go down this route.
			
			Parameters:
				public_key - Your 'public' key for myGengo. Retrieve this from your account information if you want to do authenticated calls.
				private_key - Your 'private' key for myGengo. Retrieve this from your account information if you want to do authenticated calls.
				sandbox - Whether to use the myGengo sandbox or not. Check with myGengo for the differences with this as it may change.
				headers - User agent header, dictionary style ala {'User-Agent': 'Bert'}
		"""
		self.api_url = api_urls['sandbox'] if sandbox is True else api_urls['base']
		self.api_version = api_version
		self.public_key = public_key
		self.private_key = private_key
		# If there's headers, set them, otherwise be an embarassing parent for their own good.
		self.headers = headers
		if self.headers is None:
			self.headers = {'User-agent': 'PyGengo Python myGengo Library v%s' % __version__}
		# No matter whether we get some supplied or use the generic, tell it we want JSON. ;P
		self.headers['Accept'] = 'application/json'
		self.client = httplib2.Http()
	
	def __getattr__(self, api_call):
		"""
			The most magically awesome block of code you'll ever see.

			Rather than list out 9 million damn methods for this API, we just keep a table (see above) of
			every API endpoint and their corresponding function id for this library. This pretty much gives
			unlimited flexibility in API support - there's a slight chance of a performance hit here, but if this is
			going to be your bottleneck... well, don't use Python. ;P

			For those who don't get what's going on here, Python classes have this great feature known as __getattr__().
			It's called when an attribute that was called on an object doesn't seem to exist - since it doesn't exist,
			we can take over and find the API method in our table. We then return a function that downloads and parses
			what we're looking for, based on the key/values passed in.

			I'll hate myself for saying this, but this is heavily inspired by Ruby's "method_missing".

			Note: I'm largely borrowing this technique from another API library/wrapper I've written in the past (Twython).
			If you happen to read both sources and find the same text... well, that's why. ;)
		"""
		def get(self, **kwargs):
			# Grab the (hopefully) existing method 'definition' to fire off from our api hash table.
			fn = apihash[api_call]
			
			# Set up a true base URL, abstracting away the need to care about the sandbox mode
			# or API versioning at this stage.
			base_url = self.api_url.replace('{{version}}', 'v%d' % self.api_version)
			
			# Go through and replace any mustaches that are in our API url with their appropriate key/value pairs...
			base = re.sub(
				'\{\{(?P<m>[a-zA-Z]+)\}\}',
				lambda m: "%s" % kwargs.get(m.group(1), '1'), # I'll just leave this here...
				base_url + fn['url']
			)
			
			# Do a check here for specific job sets - we need to support posting multiple jobs
			# at once, so see if there's an dictionary of jobs passed in, pop it out, let things go on as normal,
			# then pick this chain back up below...
			job = None
			multiple_jobs = None
			if fn['method'] == 'POST' or fn['method'] == 'PUT':
				job = kwargs.pop('job', None)
				multiple_jobs = kwargs.pop('jobs', None)

			# Build up a proper 'authenticated' url...
			#
			# Note: for further information on what's going on here, it's best to familiarize yourself
			# with the myGengo authentication API.
			query_params = dict([k, v.encode('utf-8')] for k, v in kwargs.items())
			query_params['api_key'] = self.public_key
			query_params['ts'] = int(time())
			
			# Encoding jobs becomes a bit different than any other method call, so we catch them and do a little
			# JSON-dumping action. Catching them also allows us to provide some sense of portability between the various
			# job-posting methods in that they can all safely rely on passing dictionaries around. Huzzah!
			if fn['method'] == 'POST' or fn['method'] == 'PUT':
				if api_call == 'postTranslationJob':
					query_params['data'] = json.dumps(job, separators = (',', ':'))
				else:
					query_params['jobs'] = json.dumps(multiple_jobs, separators = (',', ':'))
				query_string = json.dumps(query_params, separators=(',', ':'), sort_keys=True)
			else:
				query_string = urlencode(sorted(query_params.items(), key = itemgetter(0)))
			
			query_hmac = hmac.new(self.private_key, query_string, sha1)
			query_params['api_sig'] = query_hmac.hexdigest()
			query_string = urlencode(query_params)
			
			# Then open and load that shiiit, yo. TODO: check HTTP method and junk, handle errors/authentication
			if fn['method'] == 'POST' or fn['method'] == 'PUT':
				resp, content = self.client.request(base, fn['method'], query_string, headers = self.headers)
			else:
				resp, content = self.client.request(base + '?%s' % query_string, fn['method'], headers = self.headers)
			
			# Load this into native Python...
			results = json.loads(content)
			
			# See if we got any weird or odd errors back that we can cleanly raise on or something...
			if 'optstat' in results:
				raise PyGengoError(errors[`results['err']['code']`], results['err']['code'])
			
			# If not, screw it, return the junks!
			return json.loads(content)
			
		if api_call in apihash:
			return get.__get__(self)
		else:
			raise AttributeError, api_call
	
	@staticmethod
	def unicode2utf8(text):
		try:
			if isinstance(text, unicode):
				text = text.encode('utf-8')
		except:
			pass
		return text
