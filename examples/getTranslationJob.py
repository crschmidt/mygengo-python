# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Get the job in question; pre_mt set to 1 will give you a machine translation
# if the human translation isn't available yet. ;)
gengo.getTranslationJob(id = 42, pre_mt = 1)
