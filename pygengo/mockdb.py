"""
	A huge map of every myGengo API endpoint to a function definition in PyGengo.

	Parameters that need to be embedded in the URL are treated with mustaches, e.g:

	{{version}}, etc

	When creating new endpoint definitions, keep in mind that the name of the mustache
	will be replaced with the keyword that gets passed in to the function at call time.

	i.e, in this case, if I pass version = 47 to any function, {{version}} will be replaced
	with 47, instead of defaulting to 1 (said defaulting takes place at conversion time).
"""

# Base PyGengo API url, no need to repeat this junk...
base_url = 'http://api.twitter.com/{{version}}'

apihash  = {
	'getRateLimitStatus': {
		'url': '/account/rate_limit_status.json',
		'method': 'GET',
	},
}
