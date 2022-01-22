"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
# from nose.tools import assert_equal

# class TestPair(object):
    
#     def test(self,sol):
#         assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
#         assert_equal(sol([1,2,3,1],3),1)
#         assert_equal(sol([1,3,2,2],4),2)
#         print ('ALL TEST CASES PASSED')


def pair_sum(arr, k):
    list1 = []
    i = 0
    while i < len(arr)-1:
        for j in range(len(arr)):
            if arr[i] + arr[j] == k:
                #print((arr[i],arr[j]))
                if tuple(sorted((arr[i],arr[j]))) not in list1:
                    list1.append((arr[i],arr[j]))
            j += 1  
        i += 1
    print(list1)
    return len(set(list1))
    


print(pair_sum([1,3,2,2],4))

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

print(pair_sum([1,2,3,1],3))

print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],12))

#Run tests
# t = TestPair()
# t.test(pair_sum)