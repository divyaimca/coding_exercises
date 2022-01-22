my_list = ['a','b','c','b','d','e','n','n','m']

print(my_list)
# uniq_list = sorted(list(set(my_list)))

# print(uniq_list)

duplicates = []

for char in my_list:
  if my_list.count(char) > 1:
    duplicates.append(char)

print(list(set(duplicates)))
  