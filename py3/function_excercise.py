def highest_even(args):
  # print(args)
  # print(*args)
  evens = []
  odds = []
  for num in args:
    evens.append(num) if num % 2 == 0 else odds.insert(-1,num)
  
  return(max(evens))



print(highest_even([6,1,2,3,10,2,3,123,45,66,11,8,98,999]))