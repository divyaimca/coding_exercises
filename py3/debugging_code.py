##Debugging - Act of fidning the bug and fixing it

# 1.Use linting - Allows us to detect error before we run our code

#e.g. the redline below num 

num + 4


# 2. Use IDE/Editor

# 3. Read Errors

4 + 'fwklfnweknew

### Exceptions : nameerror, readerror, IOError, Typeerror --> 15 kind of Exceptions##

##Pythn Dbeugger - pdb - helps to interach with code

##steps:

import pdb

def add(num1,num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, 'jkfnjkeb')

## Use a, w, help , step, list, next,exit commands inside pdb







