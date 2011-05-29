# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Update a job that has an id of 42, and reject it, cite the reason, 
# add a comment, and throw up some captcha stuff. See the docs for
# more information pertaining to this method, it can do quite a bit. :)
gengo.updateTranslationJob(id = 42, action = {
	'action': 'reject', 
	'reason': 'quality', 
	'comment': 'My grandmother does better.', 
	'captcha': 'bert'
})
