list1 = [1,2,3,4,5]
list2 = (10,20,30,40,50)
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

# from functools import reduce

# def accumulator(acc, item):
#     #print(acc, item)
#     return acc + item

# print(reduce(accumulator, list1, 10))

