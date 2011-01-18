#!/usr/bin/python

"""
	PyGengo is an unofficial Python library for interfacing with the myGengo API.
	It's released under the LGPL and totally, freely available. Check it out on Github
	if you find any issues!

	Questions, comments? ryan@venodesigns.net
"""

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.0.0'

import urllib
import urllib2 import urlopen, HTTPError
import urlparse
import httplib
import httplib2
import mimetypes
import mimetools
import re

# Twython maps keyword based arguments to Twitter API endpoints. The endpoints
# table is a file with a dictionary of every API endpoint that Twython supports.
from pygengo_mockdb import base_url, apihash

# There are some special setups (like, oh, a Django application) where
# simplejson exists behind the scenes anyway. Past Python 2.6, this should
# never really cause any problems to begin with.
try:
	# Python 2.6 and up
	import json as simplejson
except ImportError:
	try:
		# Python 2.6 and below (2.4/2.5, 2.3 is not guranteed to work with this library to begin with)
		import simplejson
	except ImportError:
		try:
			# This case gets rarer by the day, but if we need to, we can pull it from Django provided it's there.
			from django.utils import simplejson
		except:
			# Seriously wtf is wrong with you if you get this Exception.
			raise Exception("PyGengo requires the simplejson library (or Python 2.6) to work. http://www.undefined.org/python/")

class TwythonError(Exception):
	"""
		Generic error class, catch-all for most PyGengo issues.
		Special cases are handled by APILimit and AuthError.

		Note: You need to explicitly import them into your code, e.g:

		from pygengo import PyGengoError, APILimitError, AuthError
	"""
	def __init__(self, msg, error_code=None):
		self.msg = msg
		if error_code == 400:
			raise APILimit(msg)
	
	def __str__(self):
		return repr(self.msg)


class APILimitError(PyGengoError):
	"""
		Raised when you've hit an API limit. Try to avoid these, read the API
		docs if you're running into issues here, PyGengo does not concern itself with
		this matter beyond telling you that you've done goofed.
	"""
	def __init__(self, msg):
		self.msg = msg
	
	def __str__(self):
		return repr(self.msg)


class AuthError(TwythonError):
	"""
		Raised when you try to access a protected resource and it fails due to some issue with
		your authentication.
	"""
	def __init__(self, msg):
		self.msg = msg
	
	def __str__(self):
		return repr(self.msg)


class PyGengo(object):
	def __init__(self, headers = None):
		"""setup(self, headers = None)

			Instantiates an instance of PyGengo. While you can have multiple instances of PyGengo going at once, this is not recommended
			practice, and this library will never be held responsible for anything myGengo may do to you if you decide to go down this route.
			
			Parameters:
				headers - User agent header, dictionary style ala {'User-Agent': 'Bert'}
		"""
		# If there's headers, set them, otherwise be an embarassing parent for their own good.
		self.headers = headers
		if self.headers is None:
			headers = {'User-agent': 'PyGengo Python myGengo Library v%s' % __version__}
		self.client = httplib2.Http()
	
	def __getattr__(self, api_call):
		"""
			The most magically awesome block of code you'll see in 2010.

			Rather than list out 9 million damn methods for this API, we just keep a table (see above) of
			every API endpoint and their corresponding function id for this library. This pretty much gives
			unlimited flexibility in API support - there's a slight chance of a performance hit here, but if this is
			going to be your bottleneck... well, don't use Python. ;P

			For those who don't get what's going on here, Python classes have this great feature known as __getattr__().
			It's called when an attribute that was called on an object doesn't seem to exist - since it doesn't exist,
			we can take over and find the API method in our table. We then return a function that downloads and parses
			what we're looking for, based on the keywords passed in.

			I'll hate myself for saying this, but this is heavily inspired by Ruby's "method_missing".
		"""
		def get(self, **kwargs):
			# Go through and replace any mustaches that are in our API url.
			fn = api_table[api_call]
			base = re.sub(
				'\{\{(?P<m>[a-zA-Z]+)\}\}',
				lambda m: "%s" % kwargs.get(m.group(1), '1'), # The '1' here catches the API version. Slightly hilarious.
				base_url + fn['url']
			)

			# Then open and load that shiiit, yo. TODO: check HTTP method and junk, handle errors/authentication
			if fn['method'] == 'POST':
				resp, content = self.client.request(base, fn['method'], urllib.urlencode(dict([k, v.encode('utf-8')] for k, v in kwargs.items())))
			else:
				url = base + "?" + "&".join(["%s=%s" %(key, value) for (key, value) in kwargs.iteritems()])
				resp, content = self.client.request(url, fn['method'])

			return simplejson.loads(content)

		if api_call in api_table:
			return get.__get__(self)
		else:
			raise AttributeError, api_call
	
	@staticmethod
	def encode_multipart_formdata(fields, files):
		BOUNDARY = mimetools.choose_boundary()
		CRLF = '\r\n'
		L = []
		for (key, value) in fields:
			L.append('--' + BOUNDARY)
			L.append('Content-Disposition: form-data; name="%s"' % key)
			L.append('')
			L.append(value)
		for (key, filename, value) in files:
			L.append('--' + BOUNDARY)
			L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
			L.append('Content-Type: %s' % mimetypes.guess_type(filename)[0] or 'application/octet-stream')
			L.append('')
			L.append(value)
		L.append('--' + BOUNDARY + '--')
		L.append('')
		body = CRLF.join(L)
		content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
		return content_type, body
	
	@staticmethod
	def unicode2utf8(text):
		try:
			if isinstance(text, unicode):
				text = text.encode('utf-8')
		except:
			pass
		return text
