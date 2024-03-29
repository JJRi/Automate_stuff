#!/usr/bin/python3

#Chapter 7 final practise work
import re, pyperclip

#for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   # possible area code and separator
    (\s.|-|\.)?
    (\d{3})     # first 3 digits
    (s|-|\.)    # separator possible
    (\d{4})     # four digits
    (s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-0._%/+-]+   # username portion
    @
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})     # dot something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')






