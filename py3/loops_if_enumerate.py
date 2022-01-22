a = list(range(1,11))

sum = 0
for num in a:
  print(f'Now adding {num} with {sum}')
  sum += num
print(f'Total sum is {sum}')



for _ in range(0,100):
  print(_)

for i,char in enumerate("Hello"):
  print(i,char)

for i,num in enumerate(list(range(100))):
  if num == 50:
    print(f'Index of {num} is :  {i}')
    break


  