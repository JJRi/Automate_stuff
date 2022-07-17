#!/usr/bin/python3

import re

#searches are case sensetive

#you can ignore case
robocop = re.compile(r'robocop', re.IGNORECASE)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

#substitute frases
namesRegex = re.compile(r'Agent \w+')
frase = namesRegex.sub('CENSORED', 'Agent Alice is dangerous and Agent Bob is not')
print(frase)

#substitute partly with groups
agentRegex = re.compile(r'Agent (\w)\w*')
frase2 = agentRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(frase2)






