def fibonacci1(n):
    # return a list of fibonacci numbers
    if n <= 1:
        return n
    else:
        return(fibonacci1(n-1)+fibonacci1(n-2))
    
def fibonacci(n):
#n = 5
    li = []
    for n in range(n):
        print(fibonacci1(n))
        li.append(fibonacci1(n))

    return li

cube = lambda y: pow(y,3)

#print(list(map(cube,li)))

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))