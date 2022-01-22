def large_cont_sum(arr):
    if len(arr) == 0: return False
    max_sums = []
    sum = i = 0
    a = sorted(arr)
    while i < len(a):
        for num in a:
            #print(len(a))
            sum += num
        a.remove(a[i])
        if len(a) == 1:
            sum = a[i]
        #print(a)
        max_sums.append(sum)
        sum = 0
        i += 1
    #print(max_sums)
    return max(max_sums)





    #pass


print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
print(large_cont_sum([1,2,-1,3,4,-1]))
print(large_cont_sum([-1,1]))