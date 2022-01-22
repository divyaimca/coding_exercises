

new_list = ['a', 'b', 'c']
print(new_list[1]) #b
print(new_list[-2]) #b
print(new_list[1:3]) #b,c,
new_list[0] = 'z' #
print(new_list) #z,b,c

my_list = [1,2,3]
bonus = my_list + [5] #1,2,3,5 
my_list[0] = 'z' #
print(my_list) #z,1,2,3
print(bonus) #1,2,3,5 

new_list.sort()

print(new_list)


print(2 in [1,2,3])
print(3 not in [1,2,3])


a = [1,2,3]
b = [1,2,3]
c = [3,4,5]

print(a is b)
print(b is c)

a = [1,6,4,7,8]
print(a)
print(sorted(a))
print(a.sort())
a.sort()
print(a)
print(b)
b = a.copy()
print(b)
print(b[::-1])
b.reverse()
print(b)



s = ["a","b","f"]

string = " $ "
s1 = string.join(s)
print(s1)
