# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Get all the comments on a specific job.
# Note that this returns a data set, so while we just print it below, you'll
# inevitably want to iterate over it and such. 
print gengo.getTranslationJobComments(id = 42)
