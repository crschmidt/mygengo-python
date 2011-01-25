#!/usr/bin/python

"""
	A set of tests for pyGengo. They all require internet connections.
	In fact, this entire library and API requires an internet connection.
	Don't complain.

	Also keep in mind that all the test cases test against the Sandbox API,
	since... well, it makes more sense to do that. If you, for some odd reason,
	want/need to test against the regular API, modify the SANDBOX flag at the top
	of this file.

	-- Ryan McGrath (ryan @ venodesigns dat net)
"""

import unittest
from pygengo import PyGengo, PyGengoError, PyGengoAuthError

# test_keys is a file I use to store my keys separately. It's stuck in the
# .gitignore as well, so feel free to use it for your own purposes, but there's
# no warranty with this. Keys are needed to run the tests below, though, so if want to
# run the tests, copy over the example keys file and throw your information in.
#
# e.g, cp test_keys_example.py test_keys.py
from test_keys import public_key, private_key

# We test in the myGengo sandbox for all these tests. Flip this if you need/want to.
SANDBOX = True

class TestPyGengoCore(unittest.TestCase):
	"""
		Handles testing the core parts of pyGengo (i.e, authentication signing, etc).
	"""
	def test_MethodDoesNotExist(self):
		myGengo = PyGengo(public_key = public_key, private_key = private_key, sandbox = SANDBOX)
		# With how we do functions, AttributeError is a bit tricky to catch...
		self.assertRaises(AttributeError, getattr, myGengo, 'bert')
	
	def test_PyGengoAuthNoCredentials(self):
		myGengo = PyGengo(public_key = '', private_key = '', sandbox = SANDBOX)
		self.assertRaises(PyGengoError, myGengo.getAccountStats)
	
	def test_PyGengoAuthBadCredentials(self):
		myGengo = PyGengo(public_key = 'bert', private_key = 'beeeerrrttttt', sandbox = SANDBOX)
		self.assertRaises(PyGengoAuthError, myGengo.getAccountStats)


class TestAccountMethods(unittest.TestCase):
	"""
		Tests the methods that deal with retrieving basic information about
		the account you're authenticating as. Checks for one property on each
		method; if your keys work with these methods, well...
	"""
	def test_getAccountStats(self):
		myGengo = PyGengo(public_key = public_key, private_key = private_key, sandbox = SANDBOX)
		stats = myGengo.getAccountStats()
		self.assertEqual(stats['opstat'], 'ok')
	
	def test_getAccountBalance(self):
		myGengo = PyGengo(public_key = public_key, private_key = private_key, sandbox = SANDBOX)
		balance = myGengo.getAccountBalance()
		self.assertEqual(balance['opstat'], 'ok')


class TestLanguageServiceMethods(unittest.TestCase):
	"""
		Tests the methods that deal with getting information about language-translation
		service support from myGengo.
	"""
	def test_getServiceLanguagePairs(self):
		myGengo = PyGengo(public_key = public_key, private_key = private_key, sandbox = SANDBOX)
		resp = myGengo.getServiceLanguagePairs()
		self.assertEqual(resp['opstat'], 'ok')
	
	def test_getServiceLanguages(self):
		myGengo = PyGengo(public_key = public_key, private_key = private_key, sandbox = SANDBOX)
		resp = myGengo.getServiceLanguages()
		self.assertEqual(resp['opstat'], 'ok')


class TestTranslationJobFlow(unittest.TestCase):
	"""
		Tests the flow of creating a job, updating it, getting the details, and then 
		deleting the job. This is the thick of it!

		Flow is as follows:

			1: Create a mock job and get an estimate for it (setUp)
			2: Create three jobs - 1 single, 2 batched
			3: Update the first job with some arbitrary information
			4: Post a comment on the first job
			5: Post some feedback on the first job
			6: Perform a hell of a lot of GETs to the myGengo API to check stuff
			7: Delete the job if all went well (teardown phase)
			4: Update the first one with some arbitrary information
	"""
	def setUp(self):
		# First we'll create three jobs - one regular, and two at the same time...
		self.myGengo = PyGengo(public_key = public_key, private_key = private_key, sandbox = SANDBOX)
		
		# Build up and store all the values we want, because we'll wanna make sure these got set later.
		self.body_src = "Somewhere, somehow, somebody must've kicked you around some... who knows, maybe you were kidnapped, tied up, taken away, held for ransom."
		self.lc_src = 'ja'
		self.tier = 'standard'
		self.comment = 'These are lyrics to a Tom Petty song.'
		
		self.job = {
			'body_src': self.body_src,
			'lc_src': self.lc_src,
			'tier': self.tier,
			'comment': self.comment,
			'auto_approve': 0,
			'custom_data': 'Test data from the pyGengo Python Library.',
		}
		
		# Now that we've got the job, let's go ahead and see how much it'll cost.
		cost_assessment = self.myGengo.determineTranslationCost([job])
		print cost_assessment


if __name__ == '__main__':
	unittest.main()
