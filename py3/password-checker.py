name = input('What is your name : ')
password = input('Please enter your password : ')

cnt = len(password)

hash = cnt*'*'

print(f'Hey {name}, your password {hash} is {cnt} chracter long')