def fibonacci(n):
    # return a list of fibonacci numbers
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))


n = int(input('input a number : '))
for i in range(n):
    print(fibonacci(i))

