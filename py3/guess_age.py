import datetime
birth_year = int(input('Which year you were born:'))


current_year = datetime.datetime.now().date().year
if birth_year > current_year:
  print('Wrong Input, try again')
  exit()

age = current_year - birth_year

print(f'Hi there, your age is {age}')