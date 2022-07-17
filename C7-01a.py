#!/usr/bin/python3

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')

mo = phoneNumRegex.search('My phone number is 415-555-0666')
print(f'Phone number found '+mo.group())

print('Group 1:'+mo.group(1))
print('Group 2:'+mo.group(2))
print('Group 0:'+mo.group(0))

areaCode, mainNumber = mo.groups()
print(areaCode)



