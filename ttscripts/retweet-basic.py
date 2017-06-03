#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2016
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.4 or later.
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

from license import __author__
from license import __copyright__
from license import __copyrighta__
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >= 2:
    twid0 = sys.argv[1]
elif l < 2:
    twid0 = input("ID number of tweet to retweet: ")
else:
    twid0 = input("ID number of tweet to retweet: ")

try:
    twid = int(twid0)
except:
    twid1 = twid0.split("/")
    twid = twid1[-1]

try:
    twitter.retweet(id=twid)
except TwythonError as e:
    print(e)
