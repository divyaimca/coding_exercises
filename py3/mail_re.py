import re



li = ['harsh@gmail', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com', 'jbfjkb@88283.com']

l = list(filter(lambda x: re.match(r'^[a-zA-Z0-9\S]+@[a-z]+.com',x),li))

print(l)