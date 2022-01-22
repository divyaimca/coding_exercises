import re

string1 = "search this inside of this text"

print('text' in string1)

#OR

re.search('text', string1) ##Memory object


print(re.search('text', string1)) ## Returns where the substring is stored in the string


##OR

a = re.search('text', string1)

print(a)
print(a.span())   ## Where the substring occurs, the start and end index of substring
print(a.group(0))  ## Matched object ==> more useful when doing multile searches
print(a.start())  ## Where the substring occurs, the start  index of substring
print(a.end())    ## Where the substring matchh ends, the end undex of the substring

b = re.search('textee', string1)    ### substring with no match return NONE
print(b)           

###More advanced with creating pattern

pattern = re.compile('this')  ## COmpile a regex for mathing

c = pattern.search(string1)   ### Match object
print(c)
d = pattern.findall(string1)  ###
print(d)
e = pattern.fullmatch(string1)
print(e)

pattern1 = re.compile('search inside of this text')
pattern3 = re.compile('search inside of this text!')

f = pattern1.fullmatch(string1)
print(f)

g = pattern3.match(string1)
print(g)


string5 = """
Hello PDK
Hello Ramu
Hi Priya
"""
pattern = re.compile('([a-zA-Z]+)\s(\w+)')  ## ANy regex here for matching, ums, chars,

print(pattern.findall(string5))
a = pattern.search(string5).groups()
b = pattern.match(string5)

print(a)
print(b)