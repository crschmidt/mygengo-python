# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Post a comment on a specific job; perhaps you have an update for the translator
# or something of the sort.
gengo.postTranslationJobComment(id = 42, comment = {
	'body': 'I love lamp!',
})
