# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# This method is a bit tricky; you can call it like below, but how you treat
# the returned data is very much up to you.
gengo.getTranslationJobPreview(id = 42)
