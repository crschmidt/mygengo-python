# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# If you have one job id, but want to get the id of every other job that
# was submitted with it, you can do this.
print gengo.getTranslationJobBatch(id = 42)
