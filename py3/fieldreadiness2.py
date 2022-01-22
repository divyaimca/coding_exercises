from random import *
def loop_task1():
    mystring = "Secret agents are super good at staying hidden."
    for i in [x for x in mystring.split() if x[0] in ['s','S']]: print(i)

def loop_task2():
    mystring = "Secret agents are super good at staying hidden."
    for i in [x for x in mystring.split() if len(x)%2 == 0]: print(i)

def loop_task3():
    mystring = "Secret agents are super good at staying hidden."
    print([x[0] for x in mystring.split()])

def task4():
    print([x for x in range(0,11) if x%2 == 0])

def task6():
    my_list = []
    for i in range(0,10):
        my_list.append(randint(0,100))
    print(my_list)
def task7():
    print([randint(0,100) for i in range(0,10)])

def task8():
    while True:
        num = input("Please provide an even number: ")
        if int(num) % 2 == 0:
            print("Thank you")
            break

if __name__ == '__main__':
    # loop_task1()
    #loop_task2()
    #loop_task3()
    #task4()
    #task6()
    #task7()
    task8()
