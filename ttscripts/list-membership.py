#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright (C) Benjamin D. McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
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
__version__ = "0.0.1"
from license import __bitcoin__

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l == 1:
    target = input("Enter username or user ID of user: ")
elif l >= 2:
    target = sys.argv[1]

try:
    user = int(target)
except:
    user = target

if isinstance(user, str) is True:
    try:
        data = twitter.get_list_memberships(screen_name=user, count=1000)
    except TwythonError as e:
        print(e)
elif isinstance(user, int) is True:
    try:
        data = twitter.get_list_memberships(user_id=user, count=1000)
    except TwythonError as e:
        print(e)

for i in range(len(data["lists"])):
    print("""          Source:  %s
            Name:  %s
             URL:  %s
List description:  %s
""" % (data["lists"][i]["user"]["screen_name"], data["lists"][i]["user"]["name"], "https://twitter.com"+data["lists"][i]["uri"], data["lists"][i]["description"]))
