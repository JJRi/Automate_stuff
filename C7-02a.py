#!/usr/bin/python3

import re

#conditional search with 0 or 1
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My phone number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 556-0666')
print(mo2.group())

#conditional zero or many
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The movie about Batwowowowoman')
print(mo3.group())

#one or many with + 
batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The movie about Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The adventures of Batman')
if mo3 == None:
    print('True')





