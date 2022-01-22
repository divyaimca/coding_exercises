##Anonymous functions, define and use them in a single line
##It has to be used only one, so we dont need to give it a name


##syntax    lambda param: action(param)
from functools import reduce

my_list = [1,2,3,4,5]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))


y_list = ['1','2','3','4','5']

print(list(map(lambda item: int(item), y_list)))



