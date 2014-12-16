#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import argparse
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

parser = argparse.ArgumentParser(
    prog="foad.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__title__, epilog=textwrap.dedent("""\
        You MUST place any parameter of more than one word in
        quotation marks.

        Can only be used with the old calling method with the
        equivalent of -f and -n.  If additional parameters are used
        (e.g. --extra or --sender), then the current method MUST be
        used.

        For more help run:  pydoc3 foad

        https://github.com/adversary-org/foad

        Bitcoin:  {0}

    {1}
    {2}
    """.format(__bitcoin__, version, __copyright__)))
parser.add_argument("-t", "--type", help="One word, indicates type of action to take (e.g. tweet, retweetreply, dm, etc).", action="store", required=False)
parser.add_argument("-n", "--name", help="Name of target, more than one word must be in quotation marks. May or may not include @symbol.", action="store", required=False)
parser.add_argument("-s", "--screenname", help="Name of target, more than one word must be in quotation marks. If the @ symbol is not included then it will be added.", action="store", required=False)
parser.add_argument("-S", "--status", help="Status ID of the tweet to reply to or retweet. If a URL is included this will be fixed in the code.", action="store", required=False)
parser.add_argument("-O", "--options", help="Lists the explicit variations (the same as: -f list_options), will accept any argument to activate.", action="store", required=False)
parser.add_argument("-V", "--version", help="Print the version number.", action="store", required=False)
