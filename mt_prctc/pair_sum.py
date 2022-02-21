def pair_sum(arr, k):
    list1 = []
    i = 0
    while i < len(arr)-1:
        for j in range(len(arr)):
            if arr[i] + arr[j] == k:
                #print((arr[i],arr[j]))
                if tuple(sorted((arr[i],arr[j]))) not in list1:
                    if arr[i] != arr[j]:
                        list1.append((arr[i],arr[j]))
            j += 1  
        i += 1
    print(list1)
    return len(set(list1))
    

print(pair_sum([1, 2, 3, 4, 5, 6, 7], 8))

print(pair_sum([1,3,2,2],4))

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

print(pair_sum([1,2,3,1],3))

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],12))