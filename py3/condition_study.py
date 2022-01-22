
is_friend = False

output = "Messaging allowed" if is_friend else "Messaging not allowed"

print(output)


is_magician = False
is_expert = True

if is_magician and is_expert:
  print('You are an expert magician')
elif is_magician and not is_expert:
  print("at least you are getting there")
elif not is_magician:
  print('You need magic powers')

print(10 == 10.0)

print(10 is 10.0)

print(10 is 10)

print('1' is '1')

print([] is []) ## Different in memory location

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)



  