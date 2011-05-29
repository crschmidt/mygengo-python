# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# Get an instance of MyGengo to work with...
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)

# Post over a job for translation.
gengo.postTranslationJob(job = {
    'type': 'text', # REQUIRED. Type to translate, you'll probably always put 'text' here. ;P
    'slug': 'Single :: English to Japanese', # REQUIRED. Slug for internally storing, can be generic.
    'body_src': 'Testing myGengo API library calls.', # REQUIRED. The text you're translating. ;P
    'lc_src': 'en', # REQUIRED. source_language_code (see getServiceLanguages() for a list of codes)  
    'lc_tgt': 'ja', # REQUIRED. target_language_code (see getServiceLanguages() for a list of codes)
    'tier': 'standard', # REQUIRED. tier type ("machine", "standard", "pro", or "ultra")
    
    'auto_approve': 0, # OPTIONAL. Hopefully self explanatory (1 = yes, 0 = no),
    'comment': 'HEY THERE TRANSLATOR', # OPTIONAL. Comment to leave for translator.
    'callback_url': 'http://...', # OPTIONAL. Callback URL that updates are sent to.
	'custom_data': 'your optional custom data, limited to 1kb.' # OPTIONAL
})
