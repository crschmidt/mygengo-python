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


Question, Comments, Complaints, Praise?
------------------------------------------------------------------------------------------------------
If you have questions or comments and would like to reach me directly, please feel free to do
so at the following outlets.

Email: ryan [at] venodesigns dot net  
Twitter: **[@ryanmcgrath](http://twitter.com/ryanmcgrath)**  
Web: **[Veno Designs - Personal Site](http://venodesigns.net/)**  

If you come across any issues, please file them on the **[Github project issue tracker](https://github.com/ryanmcgrath/pygengo/issues)**. Thanks!


Documentation
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
- _job_: Required. A dictionary containing a full job description for myGengo.

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


PyGengo.postTranslationJobs()
----------------------------------------------------------------------------------------------------------
Submits a job or group of jobs to translate.

### Parameters:
- _jobs_: Required. An Array of Jobs to run up to myGengo.
- _as_group_: Optional. 1 (true) / 0 (false, default). Whether all jobs in this group should be done by one translator. Some restrictions apply to what jobs can be grouped, including the requirement that language pairs and tiers must be the same across all jobs.
- _process_: 1 (true, default) / 0 (false). Whether to pay for the job(s) and make them available for translation.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	job1 = {
        'body_src': 'REQUIRED. The job I want translated ohgod',
        'lc_src': 'REQUIRED. source_language_code (see getServiceLanguages() for a list of codes)',
        'tier': 'REQUIRED. Quality level ("machine", "standard", "pro", "ultra")',
        'comment': 'Optional. Comment to send to the translator (instructions, etc).',
        'callback_url': 'Optional. A url to send/HTTP-POST updates to.',
        'auto_approve': 'Optional. 1 (true) or (0) false, whether to automatically approve after translation. Defaults to false, completed jobs will await review and approval by customer for 72 hours.',
        'custom_data': 'Optional. Up to 1K of storage for client-specific data that may be helpful for you to have mapped to this job.',
    }
    
	job2 = {
        'body_src': 'REQUIRED. The job I want translated ohgod',
        'lc_src': 'REQUIRED. source_language_code (see getServiceLanguages() for a list of codes)',
        'tier': 'REQUIRED. Quality level ("machine", "standard", "pro", "ultra")',
        'comment': 'Optional. Comment to send to the translator (instructions, etc).',
        'callback_url': 'Optional. A url to send/HTTP-POST updates to.',
        'auto_approve': 'Optional. 1 (true) or (0) false, whether to automatically approve after translation. Defaults to false, completed jobs will await review and approval by customer for 72 hours.',
        'custom_data': 'Optional. Up to 1K of storage for client-specific data that may be helpful for you to have mapped to this job.',
    }
    
	# Post over our two jobs, use the same translator for both, don't pay for them
	myGengo.postTranslationJobs(jobs = [job1, job2], as_group = 1, process = 0)


PyGengo.determineTranslationCost()
----------------------------------------------------------------------------------------------------------
Determine how much it'll cost to translate a given piece of text/copy. A method that believes it's a POST, even though
it very much seems like a GET. Bears a striking similarity to PyGengo.postTranslationJobs().

### Parameters:
- _jobs_: Required. An Array of Jobs to run up to myGengo.

### Example:	
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	job1 = {
        'body_src': 'REQUIRED. The job I want translated ohgod',
        'lc_src': 'REQUIRED. source_language_code (see getServiceLanguages() for a list of codes)',
        'tier': 'REQUIRED. Quality level ("machine", "standard", "pro", "ultra")',
        'comment': 'Optional. Comment to send to the translator (instructions, etc).',
        'callback_url': 'Optional. A url to send/HTTP-POST updates to.',
        'auto_approve': 'Optional. 1 (true) or (0) false, whether to automatically approve after translation. Defaults to false, completed jobs will await review and approval by customer for 72 hours.',
        'custom_data': 'Optional. Up to 1K of storage for client-specific data that may be helpful for you to have mapped to this job.',
    }
    
	job2 = {
        'body_src': 'REQUIRED. The job I want translated ohgod',
        'lc_src': 'REQUIRED. source_language_code (see getServiceLanguages() for a list of codes)',
        'tier': 'REQUIRED. Quality level ("machine", "standard", "pro", "ultra")',
        'comment': 'Optional. Comment to send to the translator (instructions, etc).',
        'callback_url': 'Optional. A url to send/HTTP-POST updates to.',
        'auto_approve': 'Optional. 1 (true) or (0) false, whether to automatically approve after translation. Defaults to false, completed jobs will await review and approval by customer for 72 hours.',
        'custom_data': 'Optional. Up to 1K of storage for client-specific data that may be helpful for you to have mapped to this job.',
    }
    
	# Post over our two jobs, use the same translator for both, don't pay for them
	myGengo.determineTranslationCost(jobs = [job1, job2])


PyGengo.updateTranslationJob()
----------------------------------------------------------------------------------------------------------
Updates an existing job. A bit of a hamburger method in that you can cook this one many different ways - pay
attention to the parameter specifications.

### Parameters:
- _id_: Required. The ID of the job you're updating.
- _action_: Required. The action you are performing on this job ("purchase", "revise", "approve", "reject"). Some
of these actions require other parameters, see their respective sections immediately below.

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
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.updateTranslationJob(
        id = 42,
        action = "approve",
        rating = 4,
        for_translator = "Thank You So Much!",
        for_mygengo = "Yeeaaahhh you did",
        public = 1
    )


PyGengo.getTranslationJob()
----------------------------------------------------------------------------------------------------------
Retrieves a specific job from myGengo.

### Parameters:
- _id_: Required. The ID of the job you want to retrieve.
- _pre_mt_: Optional. 1 (true) / 0 (false, default). Whether to return a machine translation if the human translation is not complete yet.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJob(id = 42, pre_mt = 1)


PyGengo.getTranslationJobs()
----------------------------------------------------------------------------------------------------------
Retrieves a list of resources for the most recent jobs filtered by the given parameters.

### Parameters:
- _status_: Optional. "unpaid", "available", "pending", "reviewable", "approved", "rejected", or "canceled".
- _timestamp_after_: Optional. Epoch timestamp from which to filter submitted jobs.
- _count_: Optional. Defaults to 10.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobs(status = "unpaid", count = 15)


PyGengo.getTranslationJobBatch()
----------------------------------------------------------------------------------------------------------
Retrieves the group of jobs that were previously submitted together.

### Parameters:
- _id_: Required. The ID of a job that you're looking for the entire batch of.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobBatch(id = 42)


PyGengo.postTranslationJobComment()
----------------------------------------------------------------------------------------------------------
Submits a new comment to the job's comment thread.

### Parameters:
- _id_: Required. The ID of the translation job to comment on.
- _body_: Required. The body/text of your comment.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.postTranslationJobComment(id = 42, body = 'I love lamp!')


PyGengo.getTranslationJobComments()
----------------------------------------------------------------------------------------------------------
Retrieves the comment thread for a job.

### Parameters:
- _id_: Required. The ID of the translation job you're retrieving comments from.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobComments(id = 42)


PyGengo.getTranslationJobFeedback()
-----------------------------------------------------------------------------------------------------------
Retrieves the feedback you have submitted for a particular job.

### Parameters:
- _id_: Required. The ID of the translation job you're retrieving comments from.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobFeedback(id = 42)


PyGengo.getTranslationJobRevisions()
-------------------------------------------------------------------------------------------------------------
Gets list of revision resources for a job. Revisions are created each time a translator or Senior Translator updates the text.

### Parameters:
- _id_: Required. The ID of the translation job you're getting revisions from.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobRevisions(id = 42)


PyGengo.getTranslationJobRevision()
----------------------------------------------------------------------------------------------------------
Gets a specific revision for a job.

### Parameters:
- _id_: Required. The ID of the translation job you're getting revisions from.
- _rev_id_: Required. The ID of the revision you're looking up.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobRevision(id = 42, rev_id = 1)


PyGengo.getTranslationJobPreviewImage()
----------------------------------------------------------------------------------------------------------
Renders a GIF preview image of the translated text.

### Parameters:
- _id_: Required. The ID of the translation job you want a preview image for.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getTranslationJobPreview(id = 42)


PyGengo.deleteTranslationJob()
----------------------------------------------------------------------------------------------------------
Cancels the job. You can only cancel a job if it has not been started already by a translator.

### Parameters:
- _id_: Required. The ID of the job you want to delete.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.deleteTranslationJob(id = 42)


PyGengo.getServiceLanguages()
----------------------------------------------------------------------------------------------------------
Returns a list of supported languages and their language codes.

### Paramters:
None

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
	myGengo.getServiceLanguages()


PyGengo.getServiceLanguagePairs()
--------------------------------------------------------------------------------------------------------
Returns supported translation language pairs, tiers, and credit prices.

### Parameters:
- _lc_src_: Optional. A source language code to filter the results to relevant pairs.

### Example:
    from pygengo import PyGengo
    
    myGengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly False, depending on your dev needs
    )
    
    # Send along an optional source language declaration.
	myGengo.getServiceLanguagePairs(lc_src = 'en')


PyGengo.unicode2utf8()
--------------------------------------------------------------------------------------------------------
Convenience method for making sure that text is in an acceptable format for myGengo submissions.

### Parameters:
- _text_: Required. Text to convert.

### Example:
    from pygengo import PyGengo    
   
    # Send along an optional source language declaration.
	PyGengo.unicode2utf8('I'm gonna convert the hell out of this text')
