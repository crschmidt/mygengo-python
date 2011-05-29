# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Useful for figuring out what language paths are supported - e.g, if
# we use 'en' below, we'll see what languages we can translate TO from 'en'.
print gengo.getServiceLanguagePairs(lc_src = 'en')
