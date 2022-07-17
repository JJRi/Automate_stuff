#!/usr/bin/python3

import re

#character classes d=digits,s=spaces,w=alphabets for words. Capitals mean not these
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge, 1tree'))

#square brackets make your own class and the hat ^ means negative
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#the in beginning means frase must start with it
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello worlds!'))

print(beginsWithHello.search('The hello sting') == None)
    
#dollar sign can match the ends
endsWithNmbr = re.compile(r'\d$')
print(endsWithNmbr.search('Yer number is 42'))
print(endsWithNmbr.search('Your number is forty two'))










