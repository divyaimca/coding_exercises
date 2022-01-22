my_list = ['a','b','c','b','d','e','n','n','m']

duplicates = list(set([char for char in my_list if my_list.count(char) > 1]))

print(duplicates)