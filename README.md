myGengo Python Library (for the [myGengo API](http://mygengo.com/))
========================================================================================================
Translating your tools and products helps people all over the world access them; this is, of course, a
somewhat tricky problem to solve. **[myGengo](http://mygengo.com/)** is a service that offers human-translation
(which is often a higher quality than machine translation), and an API to manage sending in work and watching
jobs. This is a python interface to make using the API simpler (some would say incredibly easy). 

Installation & Requirements
-------------------------------------------------------------------------------------------------------
Installing myGengo is fairly simple:

    pip install mygengo

Alternatively, if you're in the stone ages:

    easy_install mygengo

myGengo also relies on httplib2, which can be installed through either of the above methods. If
you're running on a version of Python prior to 2.6, you'll need to install simplejson as well.

A version of myGengo for Python 3 is in the works, but as Python 3 isn't even quite deemed production
ready/reliable yet, it's not the highest priority at the moment.


Tests - Running Them, etc
------------------------------------------------------------------------------------------------------
myGengo has a full suite of Unit Tests. To run them, grab the source, head into the mygengo directory, 
and execute the tests file with the Python interpreter, ala:

    python tests.py


Question, Comments, Complaints, Praise?
------------------------------------------------------------------------------------------------------
If you have questions or comments and would like to reach us directly, please feel free to do
so at the following outlets. We love hearing from developers!

Email: ryan [at] mygengo dot com  
Twitter: **[@mygengo_dev](http://twitter.com/mygengo_dev)**  

If you come across any issues, please file them on the **[Github project issue tracker](https://github.com/myGengo/mygengo-python/issues)**. Thanks!


Documentation
-----------------------------------------------------------------------------------------------------
**Full documentation of each function is below**, but anyone should be able to cobble together 
a working script with the following:

``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly false, depending on your dev needs
)
    
print gengo.getAccountBalance()
```

All function definitions can be found inside mygengo/mockdb.py. They exist as an uber dictionary: the
key of the dictionary entry is the function name, and the parameters are exactly the same as specified
over on the **[myGengo API docs](http://mygengo.com/about/services/api)**.

MyGengo()
---------------------------------------------------------------------------------------------------
Creates an instance of MyGengo for you to communicate with the myGengo API. This needs to be done
before any of the methods below are available.

#### Parameters:
- _public_key_: Required. Your public key, generated on the myGengo API site.
- _private_key_: Required. Your private key, generated on the myGengo API site.
- _sandbox_: Optional. Defaults to False, dictates whethe to send the call to the myGengo Sandbox API.
- _api_version_: Optional. API version to use with myGengo (defaults to 1).
- _headers_: Optional. Additional HTTP headers to send along, passed as a dictionary object.  

#### Example:   
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)
```

MyGengo.getAccountStats()
---------------------------------------------------------------------------------------------------
Retrieves your account stats, like orders made, etc.

#### Parameters:
None  

### Example:  
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

print gengo.getAccountStats()
```

MyGengo.getAccountBalance()
--------------------------------------------------------------------------------------------------
Retrieves your account balance in myGengo credits.

### Parameters:
None

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

print gengo.getAccountBalance()
```

MyGengo.postTranslationJob()
---------------------------------------------------------------------------------------------------
Sends a new job over to myGengo for translation. Jobs are dictionaries that get passed around; an example is
below.

### Parameters:
- _job_: Required. A dictionary containing a full job description for myGengo (**see below**).

### Example:
``` python    
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

job = {
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
}

gengo.postTranslationJob(job = job)
```

MyGengo.postTranslationJobs()
----------------------------------------------------------------------------------------------------------
Submits a job or group of jobs to translate.

### Parameters:
- _jobs_: Required. A Dictionary of jobs and associated properties to run up to myGengo.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

data = {
	'jobs': {
		'job_1': {
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
		},
		'job_2': {
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
		},
    },
	'process': 1, # OPTIONAL. 1 (true, default) / 0 (false). Whether to pay for the job(s) and make them available for translation.
    'as_group': 1, # OPTIONAL. 1 (true) / 0 (false, default). Whether all jobs in this group should be done by one translator.
}

# Post over our two jobs, use the same translator for both, don't pay for them
gengo.postTranslationJobs(jobs = data)
```
**Note:** 'as_group' has a catch: some restrictions apply to what jobs can be grouped, including the requirement that language pairs and tiers must be the same across all jobs.


MyGengo.determineTranslationCost()
----------------------------------------------------------------------------------------------------------
Determine how much it'll cost to translate a given piece of text/copy. A method that believes it's a POST, even though
it very much seems like a GET. Bears a striking similarity to MyGengo.postTranslationJobs().

### Parameters:
- _jobs_: Required. An Dictionary of Jobs to run up to myGengo.

### Example:	
``` python
from mygengo import MyGengo
   
gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)
   
jobs_data = {
	'job_1': {
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
	},
    'job_2': {
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
     },
}
   
# Post over our two jobs, use the same translator for both, don't pay for them
gengo.determineTranslationCost(jobs = jobs_data)
```

MyGengo.updateTranslationJob()
----------------------------------------------------------------------------------------------------------
Updates an existing job. A bit of a hamburger method in that you can cook this one many different ways - pay
attention to the parameter specifications.

### Parameters:
- _id_: Required. The ID of the job you're updating.
- _action_: Required. A dictionary describing the actions you are performing on this job ("purchase", "revise", "approve", "reject"). Some
of these actions require other parameters, see their respective sections immediately below.

### "purchase" Parameters:
None

### "revise" Parameters:
- _comment_: Optional. A comment describing the revision.

### "approve" Parameters:
- _rating_: Required. 1 - 5, 1 = ohgodwtfisthis, 5 = I want yo babies yo,
- _for_translator_: Optional. Comments that you can pass on to the translator.
- _for_mygengo_: Optional. Comments to send to the myGengo staff (kept private on myGengo's end)
- _public_: Optional. 1 (true) / 0 (false, default). Whether myGengo can share this feedback publicly.

### "reject" Parameters:
- _reason_: Required. Reason for rejection (must be "quality", "incomplete", "other")
- _comment_: Required. Explain your rejection, especially if all you put was "other".
- _captcha_: Required. The captcha image text. Each job in a "reviewable" state will have a captcha_url value, which is a URL to an image. This captcha value is required only if a job is to be rejected. If the captcha is wrong, a URL for a new captcha is also included with the error message.
- _follow_up_: Optional. "requeue" (default) or "cancel". If you choose "requeue" the job will be rejected and then passed onto another translator. If you choose "cancel" the job will be completely cancelled upon rejection.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

# Some example action objects, choose one to test by uncommenting
updateObj = {'action': 'purchase'}
# updateObj = {'action': 'revise', 'comment': 'Thanks but no thanks'}
# updateObj = {'action': 'approve', 'rating': 1, 'for_translator': 'Thanks!'}
# updateObj = {'action': 'reject', 'reason': 'quality', 'comment': 'My grandmother does better.', 'captcha': 'bert'}

gengo.updateTranslationJob(id = 42, action = updateObj)
```

MyGengo.getTranslationJob()
----------------------------------------------------------------------------------------------------------
Retrieves a specific job from mygengo.

### Parameters:
- _id_: Required. The ID of the job you want to retrieve.
- _pre_mt_: Optional. 1 (true) / 0 (false, default). Whether to return a machine translation if the human translation is not complete yet.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJob(id = 42, pre_mt = 1)
```

MyGengo.getTranslationJobs()
----------------------------------------------------------------------------------------------------------
Retrieves a list of resources for the most recent jobs filtered by the given parameters.

### Parameters:
- _status_: Optional. "unpaid", "available", "pending", "reviewable", "approved", "rejected", or "canceled".
- _timestamp_after_: Optional. Epoch timestamp from which to filter submitted jobs.
- _count_: Optional. Defaults to 10.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobs(status = "unpaid", count = 15)
```

MyGengo.getTranslationJobBatch()
----------------------------------------------------------------------------------------------------------
Retrieves the group of jobs that were previously submitted together.

### Parameters:
- _id_: Required. The ID of a job that you're looking for the entire batch of.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobBatch(id = 42)
```


MyGengo.postTranslationJobComment()
----------------------------------------------------------------------------------------------------------
Submits a new comment to the job's comment thread.

### Parameters:
- _id_: Required. The ID of the translation job to comment on.
- _comment_: Required. A dictionary with the body/text of your comment.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.postTranslationJobComment(id = 42, comment = {
	'body': 'I love lamp!',
})
```

MyGengo.getTranslationJobComments()
----------------------------------------------------------------------------------------------------------
Retrieves the comment thread for a job.

### Parameters:
- _id_: Required. The ID of the translation job you're retrieving comments from.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobComments(id = 42)
```

MyGengo.getTranslationJobFeedback()
-----------------------------------------------------------------------------------------------------------
Retrieves the feedback you have submitted for a particular job.

### Parameters:
- _id_: Required. The ID of the translation job you're retrieving comments from.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobFeedback(id = 42)
```

MyGengo.getTranslationJobRevisions()
-------------------------------------------------------------------------------------------------------------
Gets list of revision resources for a job. Revisions are created each time a translator or Senior Translator updates the text.

### Parameters:
- _id_: Required. The ID of the translation job you're getting revisions from.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobRevisions(id = 42)
```

MyGengo.getTranslationJobRevision()
----------------------------------------------------------------------------------------------------------
Gets a specific revision for a job.

### Parameters:
- _id_: Required. The ID of the translation job you're getting revisions from.
- _rev_id_: Required. The ID of the revision you're looking up.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobRevision(id = 42, rev_id = 1)
```

MyGengo.getTranslationJobPreviewImage()
----------------------------------------------------------------------------------------------------------
Returns a GIF preview image of the translated text.

### Parameters:
- _id_: Required. The ID of the translation job you want a preview image for.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getTranslationJobPreview(id = 42)
```

MyGengo.deleteTranslationJob()
----------------------------------------------------------------------------------------------------------
Cancels the job. You can only cancel a job if it has not been started already by a translator.

### Parameters:
- _id_: Required. The ID of the job you want to delete.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.deleteTranslationJob(id = 42)
```

MyGengo.getServiceLanguages()
----------------------------------------------------------------------------------------------------------
Returns a list of supported languages and their language codes.

### Paramters:
None

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

gengo.getServiceLanguages()
```

MyGengo.getServiceLanguagePairs()
--------------------------------------------------------------------------------------------------------
Returns supported translation language pairs, tiers, and credit prices.

### Parameters:
- _lc_src_: Optional. A source language code to filter the results to relevant pairs.

### Example:
``` python
from mygengo import MyGengo

gengo = MyGengo(
    public_key = 'your_public_key',
    private_key = 'your_private_key',
    sandbox = True, # possibly False, depending on your dev needs
)

# Send along an optional source language declaration.
gengo.getServiceLanguagePairs(lc_src = 'en')
```

MyGengo.unicode2utf8()
--------------------------------------------------------------------------------------------------------
Convenience method for making sure that text is in an acceptable format for myGengo submissions.

### Parameters:
- _text_: Required. Text to convert.

### Example:
``` python
from mygengo import MyGengo    

# Make this into a UTF-8 encoded string...
MyGengo.unicode2utf8("私は")
```
