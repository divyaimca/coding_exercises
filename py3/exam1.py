x = 2.8
y = float(2.9)

print(x,y)

print('Hello' is 'Hello')

a = '   Hello   '
print(a)
print(a.strip())
print(a.upper())


fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#[fruits.add(i) for i in more_fruits]
print(fruits)