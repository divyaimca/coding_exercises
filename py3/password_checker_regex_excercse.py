import re
#import pdb

password_string = input('Enter the password:')

pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")

if  pattern.fullmatch(password_string):
    print('Your passwod is valid')
  #  pdb.set_trace()
else:
    print('Please inputa valid password and try again')
    print('Valid passowrd contain atleast one small letter, atleast one capital letter, atleast one special chracter from $#@% \n')

