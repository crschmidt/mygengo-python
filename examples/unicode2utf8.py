# -*- coding: utf-8 -*-
#!/usr/bin/python

from mygengo import MyGengo

# This method doesn't require an instance of MyGengo, it's
# purely utility. You'll possibly end up using it to ensure
# that your data is utf-8 encoded before submitting it to myGengo;
# if your method calls fail, this is probably the first thing you should
# check!
MyGengo.unicode2utf8("私は")
