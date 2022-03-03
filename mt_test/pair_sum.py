

def pair_sum(li,k):
    #print(li,k)

    pairs = []
    i = j = 0
    for  i in range(len(li)):
        for  j in  range(len(li)):
            a = li[i]
            b = li[j]
            if a != b and a+b == k:
                ele = sorted([a,b])
                pairs.append(tuple(ele))  



    return(len(set(pairs)))
   
def pair_sum1(arr,k):
    print(arr,k)
    pairs = []
    for  i in arr:
        j = k - i
        if j in set(arr) and i != j:
            
            ele = sorted([i,j])
            pairs.append(tuple(ele)) 


    print(set(pairs)) 

    

    







pair_sum1([1, 2, 3, 4, 5, 6, 7],8)

# print(pair_sum([1, 2, 3, 4, 5, 6, 7],8))
# print(pair_sum([1, 2, 3, 4, 5, 6, 7],98))