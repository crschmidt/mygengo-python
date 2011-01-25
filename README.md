pyGengo - a Python Library for the [myGengo API](http://myGengo.com/)
========================================================================================================
I built pyGengo because I didn't see a clear cut method for interacting with the myGengo
API in Python, and that bothered me. myGengo has an excellent API for real human-based translation
that should be getting way more love. To that end, pyGengo is released (under the LGPL), totally
free for anyone to use.

Installation & Requirements
-------------------------------------------------------------------------------------------------------
Installing pyGengo is fairly simple:

    pip install pygengo

Alternatively, if you're in the stone ages:

    easy_install pygengo

pyGengo also relies on httplib2, which can be installed through either of the above methods. If
you're running on a version of Python prior to 2.6, you'll need to install simplejson as well.

A version of pyGengo for Python 3 is in the works, but as Python 3 isn't even quite deemed production
ready/reliable yet, it's not the highest priority at the moment.


Basic Usage
-----------------------------------------------------------------------------------------------------
**Full documentation of each function is below**, but anyone should be able to cobble together 
a working script with the following:

    from pygengo import PyGengo
    
    mygengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly false, depending on your dev needs
    )
    
    print mygengo.getAccountBalance()

All function definitions can be found inside pygengo/mockdb.py. They exist as an uber dictionary: the
key of the dictionary entry is the function name, and the parameters are exactly the same as specified
over on the **[myGengo API site](http://mygengo.com/about/services/api)**.

Question, Comments, Complaints, Praise?
------------------------------------------------------------------------------------------------------
If you have questions or comments and would like to reach me directly, please feel free to do
so at the following outlets.

Email: ryan [at] venodesigns dot net  
Twitter: http://twitter.com/ryanmcgrath  
Web: http://venodesigns.net/  

If you come across any issues, please file them on the Github project issue tracker. Thanks!



PyGengo()
---------------------------------------------------------------------------------------------------
Creates an instance of pyGengo for you to communicate with the myGengo API. This needs to be done
before any of the methods below are available.

#### Parameters:
- _public_key_: Required. Your public key, generated on the myGengo API site.
- _private_key_: Required. Your private key, generated on the myGengo API site.
- _sandbox_: Optional. Defaults to False, dictates whethe to send the call to the myGengo Sandbox API.
- _api_version_: Optional. API version to use with myGengo (defaults to 1).
- _headers_: Optional. Additional HTTP headers to send along, passed as a dictionary object.  

#### Example:   
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )


PyGengo.getAccountStats()
---------------------------------------------------------------------------------------------------
Retrieves your account stats, like orders made, etc.

#### Parameters:
None  

### Example:  
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
    print myGengo.getAccountStats()


PyGengo.getAccountBalance()
--------------------------------------------------------------------------------------------------
Retrieves your account balance in myGengo credits.

### Parameters:
None

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
    print myGengo.getAccountBalance()


PyGengo.postTranslationJob()
---------------------------------------------------------------------------------------------------
Sends a new job over to myGengo for translation. Jobs are dictionaries that get passed around; an example is
below.

### Parameters:
- _job_: A dictionary containing a full job description for myGengo.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	job = {
        'body_src': 'REQUIRED. The job I want translated ohgod',
        'lc_src': 'REQUIRED. source_language_code (see getServiceLanguages() for a list of codes)',
        'tier': 'REQUIRED. Quality level ("machine", "standard", "pro", "ultra")',
        'comment': 'Optional. Comment to send to the translator (instructions, etc).',
        'callback_url': 'Optional. A url to send/HTTP-POST updates to.',
        'auto_approve': 'Optional. 1 (true) or (0) false, whether to automatically approve after translation. Defaults to false, completed jobs will await review and approval by customer for 72 hours.',
        'custom_data': 'Optional. Up to 1K of storage for client-specific data that may be helpful for you to have mapped to this job.',
    }
    
	myGengo.postTranslationJob(job)
