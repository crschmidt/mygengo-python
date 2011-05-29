#!/usr/bin/python

import sys, os
from setuptools import setup
from setuptools import find_packages

__author__ = 'Ryan McGrath <ryan@mygengo.com>'
__version__ = '1.2.0'

setup(
	# Basic package information.
	name = 'mygengo',
	version = __version__,
	packages = find_packages(),

	# Packaging options.
	include_package_data = True,

	# Package dependencies.
	install_requires = ['simplejson'],

	# Metadata for PyPI.
	author = 'Ryan McGrath',
	author_email = 'ryan@venodesigns.net',
	license = 'LGPL License',
	url = 'http://github.com/ryanmcgrath/mygengo/tree/master',
	keywords = 'mygengo translation language api japanese english',
	description = 'Official Python library for interfacing with the MyGengo API.',
	long_description = open('README.md').read(),
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Communications :: Chat',
		'Topic :: Internet'
	]
)
