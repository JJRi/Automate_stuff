#!/usr/bin/python3

import re

phoneREgex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneREgex.findall('Cell: 415-555-4242 and work is 411-411-9191')
print(mo)

#findall return tuples if there are groups
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneRegex.findall('Cell: 415-555-4242 and work is 411-411-9191')
print(mo1)






