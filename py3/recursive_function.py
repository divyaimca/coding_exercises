def recursive_function(n):
    if n == 1:
        return n
    else:
        return n * recursive_function(n-1)


print(recursive_function(100))

