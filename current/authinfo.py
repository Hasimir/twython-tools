#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.6
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x).
# * Converted from scripts initially developed with Python 2.7.x.
# * python-gnupg 0.3.6 or later.
# * GNU Privacy Guard (GnuPG, GPG) 1.4.x or 2.0.x).
# * Tor service with SOCKS and proxy (optional).
#
# Options and notes:
#
# The config.py file must be customised prior to running either
# gen-auth.py or authinfo.py in order to set the correct path for the
# GPG configuration and adjust other settings.
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.6"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import binascii
import getpass
import hashlib
import sys

from simplecrypt import encrypt, decrypt

try:
    password = getpass.getpass("Enter the passphrase to authorise access to Twitter: ")
except getpass.GetPassWarning:
    print("Your current terminal may display your password.  You will be prompted to continue or not.")
    cont = input("Do you wish to continue (yes/no): ")
    if cont.lower() == "yes" or "y":
        password = getpass.getpass("Enter the passphrase to authorise access to Twitter: ")
    else:
        print("You should use a normal xterm to run this program.")
        print("Exiting.")
        sys.exit()

phrase = hashlib.sha256(password.encode("utf-8")).hexdigest()
del password
torcon = input("Will you be using Tor to access Twitter (Y/N): ")

files = ["oauth1.txt.asc", "oauth2.txt.asc", "oauth3.txt.asc", "oauth4.txt.asc"]
authdata = []

for i in range(4):
    afile = open(files[i], "r")
    crypted = afile.read()
    afile.close()
    ciphertext = binascii.unhexlify(crypted.encode("utf-8"))
    plaintext = decrypt(phrase, ciphertext)
    authsecret = plaintext.decode("utf-8").strip()
    authdata.append(authsecret)

APP_KEY = authdata[0]
APP_SECRET = authdata[1]
OAUTH_TOKEN = authdata[2]
OAUTH_TOKEN_SECRET = authdata[3]

del phrase

affirmative = ["Y", "yes", "y", "1", "true", "aye", 1, True]
negative = ["N", "no", "n", "0", "false", "nay", 0, False]

if torcon.lower() in negative:
    client_args = {
        "verify": True,
        "headers": {
            "User-Agent": "Twython"
            }
        }
    print("No Tor configuration set, direct connection enabled.")
elif torcon.lower() in affirmative:
    tortype = input("Will you be using the Tor Browser Bundle: ")
    bundle = ["Y", "yes", "y", "1", "true", "aye", "bundle", 1, True]
    if tortype.lower() in bundle:
        client_args {
            "verify": True,
            "headers": {
                "User-Agent": "Twython Over Tor"
                },
            "proxies": {
                "http": "http://127.0.0.1:9150",
                "https": "https://127.0.0.1:9150",
                }
            }
        print("Tor configuration set on localhost and port 9150")
    else:
        client_args = {
            "verify": True,
            "headers": {
                "User-Agent": "Twython Over Tor"
                },
            "proxies": {
                "http": "http://127.0.0.1:9050",
                "https": "https://127.0.0.1:9050",
                }
            }
        print("Tor configuration set on localhost and port 9050")
else:
    client_args = {
        "verify": True,
        "headers": {
            "User-Agent": "Twython"
            }
        }
    print("No Tor configuration set, direct connection enabled.")
