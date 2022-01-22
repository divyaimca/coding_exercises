##IO throught reading nd writing to files, works with cursor

my_file = open('fileio_test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)

# print(my_file.readline())

print(my_file.readlines())



my_file.close()


with open('fileio_test.txt', mode='r+') as my_file:
    text = my_file.write('Helloooooo there \n I am pdk')
    print(text)



## Toaccess files from payth give fullpath or relative path


## use try catch to catch exception
try:
    with open('app/filetest.txt', mode='w') as myfile:
        text = myfile.write('Helloooooo there \n I am pdk')
        print(text)
except FileNotFoundError as err:
    print('file doesnot exist')
    raise err
except IOError as err:
    print('IO Error')
    raise err

