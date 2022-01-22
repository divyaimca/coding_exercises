

def file_task1(file):
    try:
        with open(file, mode='r') as my_file:
            lines = my_file.readlines()
            print(lines)
    except FileNotFoundError as err:
        print(f'{file} : File not found')
        raise err

def file_task2(file):
    try:
        with open(file, mode='r') as my_file:
            lines = my_file.readlines()
            print(len(lines))
    except FileNotFoundError as err:
        print(f'{file} : File not found')
        raise err

def file_task3(file):
    try:
        with open(file, mode='r') as my_file:
            lines = my_file.readlines()
            print(lines[4])
    except FileNotFoundError as err:
        print(f'{file} : File not found')
        raise err

def file_task4(file):
    try:
        with open(file, mode='r') as my_file:
            lines = my_file.readlines()
            print(lines[-1])
    except FileNotFoundError as err:
        print(f'{file} : File not found')
        raise err

def file_task5(file):
    try:
        with open(file, mode='r') as my_file:
            lines = my_file.readlines()
            if 'o' in lines[-1]: return('o')
    except FileNotFoundError as err:
        print(f'{file} : File not found')
        raise err

def file_task6(file):
    try:
        with open(file, mode='r') as my_file:
            lines = my_file.readlines()
            return len(lines[-1].split())
    except FileNotFoundError as err:
        print(f'{file} : File not found')
        raise err
def data_type():
    print(type(2/3))
    print(type(2+2.0))
    print(type(1+1))
    print(type("2" + "2"))
    print(type(1>2))

def data_task7():
    d = {"levelone":[1,2,{'leveltwo':[5,6,[1,['get me please']]]}]}
    print(d['levelone'][2]['leveltwo'][2][1][0])


def data_task8():
    mylist = [1,2,3,4,5,6,4,3,2,1,2,3,4,5,6,6,7,8,5,6,7,8,9,8,9,8,9,7,10,123,1,2,2,3,1,3,2,4,1,4,4,1,2,2,22,3,4,1,4,1]
    return len(set(mylist))

if __name__ == '__main__':
    # file_task1('files/exam.txt')
    # file_task2('files/exam.txt')
    # file_task3('files/exam.txt')
    # file_task4('files/exam.txt')
    # print(file_task5('files/exam.txt'))
    # print(file_task6('files/exam.txt'))
    # data_type()
    # data_task7()
    print(data_task8())