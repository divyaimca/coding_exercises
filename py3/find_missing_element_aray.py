# def finder(a, b):
#     if set(a).issuperset(set(b)):
#         return set(a).difference(set(b))
#     else:
#         return set(b).difference(set(a))


def finder(arr1, arr2):
    li = []
    arr3 = sorted(arr1)
    arr4 = sorted(arr2)
    for i,j in zip(arr3,arr4):
        if i != j:
            return i
    return arr3[-1]

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))

arr1 = [5,5,7,7]
arr2 = [5,7,7]

print(finder(arr1,arr2))



