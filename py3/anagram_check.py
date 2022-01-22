"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
# from nose.tools import assert_equal
# #import numpy as np

# class AnagramTest(object):
    
#     def test(self,sol):
#         assert_equal(sol('go go go','gggooo'),True)
#         assert_equal(sol('abc','cba'),True)
#         assert_equal(sol('hi man','hi     man'),True)
#         assert_equal(sol('aabbcc','aabbc'),False)
#         assert_equal(sol('123','1 2'),False)
#         print("ALL TEST CASES PASSED")



def anagram(s1,s2):
    result = False
    a = sorted([n for n in list(s1) if n != ' '])
    b = sorted([m for m in list(s2) if m != ' '])
    #print(a, b)
    if len(a) == len(b):
        if a == b:
            #print('Angram Found!')
            result = True
    return result
    #pass

# Run Tests
#t = AnagramTest()#
#t.test(anagram)
print(anagram('dog','gode'))
print(anagram('go go go','gggooo'))
print(anagram('hi man','hi     man'))
print(anagram('123','1 2'))
print(anagram('aabbcc','aabbc'))
print(anagram('dog','god'))
