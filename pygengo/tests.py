#!/usr/bin/python

"""
	A set of tests for pyGengo. They all require internet connections.
	In fact, this entire library and API requires an internet connection.
	Don't complain.

	-- Ryan McGrath (ryan @ venodesigns dat net)
"""

import unittest
from pygengo import PyGengo

# pygengo_creds is a file I use to store my keys separately. It's stuck in the
# .gitignore as well, so feel free to use it for your own purposes, but there's
# no warranty with this. Keys are needed to run the tests below, though, so if want to
# run the tests, copy over the example keys file and throw your information in.
#
# e.g, cp pygengo_keys_example.py pygengo_keys.py
from test_keys import public_key, private_key

class TestAccountMethods(unittest.TestCase):
	"""
		Tests the methods that deal with retrieving basic information about
		the account you're authenticating as.
	"""
