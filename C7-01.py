#!/usr/bin/python3

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')

mo = phoneNumRegex.search('My phone number is 415-555-0666')
print(f'Phone number found '+mo.group())
