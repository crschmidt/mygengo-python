pyGengo - a Python Library for the myGengo API (http://myGengo.com/)
------------------------------------------------------------------------------------------
I built pyGengo because I didn't see a clear cut method for interacting with the myGengo
API in Python, and that bothered me. myGengo has an excellent API for real human-based translation
that should be getting way more love. To that end, pyGengo is released (under the LGPL), totally
free for anyone to use.

Installation & Requirements
------------------------------------------------------------------------------------------
Installing pyGengo is fairly simple:

    pip install pygengo

Alternatively, if you're in the stone ages:

    easy_install pygengo

pyGengo also relies on httplib2, which can be installed through either of the above methods. If
you're running on a version of Python prior to 2.6, you'll need to install simplejson as well.

A version of pyGengo for Python 3 is in the works, but as Python 3 isn't even quite deemed production
ready/reliable yet, it's not the highest priority at the moment.


Basic Usage
------------------------------------------------------------------------------------------
Full in-depth documentation is coming on the Github project page wiki soon, but in the meantime
anyone should be able to cobble together a working script with the following:

    from pygengo import PyGengo
    
    mygengo = PyGengo(
        public_key = 'your_public_key',
        private_key = 'your_private_key',
        sandbox = True, # possibly false, depending on your dev needs
    )
    
    print mygengo.getAccountBalance()

All function definitions can be found inside pygengo/mockdb.py. They exist as an uber dictionary: the
key of the dictionary entry is the function name, and the parameters are exactly the same as specified
over on the myGengo API site (http://mygengo.com/about/services/api).

Question, Comments, Complaints, Praise?
-------------------------------------------------------------------------------------------
If you have questions or comments and would like to reach me directly, please feel free to do
so at the following outlets.

Email: ryan [at] venodesigns dot net  
Twitter: http://twitter.com/ryanmcgrath  
Web: http://venodesigns.net/  

If you come across any issues, please file them on the Github project issue tracker. Thanks!
