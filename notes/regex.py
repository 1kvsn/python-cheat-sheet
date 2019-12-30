# Regex

# use
https://regex101.com/

import re

string = 'search inside of this text this please!'

a = re.search('this', string) # gives match object which shows the index where the string begins and ends

# match object looks like this
# <re.Match object; span=(17, 21), match='this'>

a.span() # gives tuple of index (17, 21)
a.start() # 17
a.end() # 21

# pattern = re.compile('this') # TO BE SEARCHED
a = pattern.search(string) # WITHIN WITH IT NEEDS TO BE SEARCHED
b = pattern.findall(string) # gives a list containing number of instances the pattern was found

print(a.group()) # gives the matched text
print(b) # ['this', 'this']

# =======================================================

pattern = re.compile('search inside of this text this please!')
c = pattern.fullmatch(string) # gives match object only when it is a EXACT match
print(c) # <re.Match object; span=(0, 39), match='search inside of this text this please!'>

# ========================================================

d = pattern.match(string)
print(d) # matches the string and doesn't care what extra text is present there 
#<re.Match object; span=(0, 39), match='search inside of this text this please!'>

# ===========================================================