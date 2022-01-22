#Square
my_list = [5,4,3]

print(list(map(lambda num: num**2, my_list)))

#List Sorting
list1 = [(0,2), (4,3),(13,1), (9,9), (10,-1)]
list1.sort(key=lambda num: num[-1])
print(list1)


