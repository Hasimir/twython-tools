#!/usr/bin/env python3

##
# Copyright (C) Benjamin D. McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# 
#
#
# Requirements:
#
# * Python 3.4 or later.
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
    user = sys.argv[1]
else:
    user = input("User to block: ")

try:
    target = int(user)
except:
    target1 = user.split("/")
    target = target1[-1]

if isinstance(target, str) is True:
    try:
        twitter.destroy_mute(screen_name=target, skip_status="true")
    except TwythonError as e:
        print(e)
elif isinstance(target, int) is True:
    try:
        twitter.destroy_mute(user_id=target, skip_status="true")
    except TwythonError as e:
        print(e)
