def docstring(a):
  '''
  Info : This function retuns the type of datstructure as input.Thi is the help how the function should be used. Always pass the argument a to the function
  example:
    docstring('hello')
    docstring([1,2,3])
    docstring(1,2,3)
  '''
  return type(a)


print(docstring([1,2,3]))

docstring(1)

help(docstring)


print(docstring.__doc__)