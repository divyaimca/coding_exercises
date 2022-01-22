from itertools import *

def solution(S):
    li = []
    for x,y in combinations(range(len(S)),r=2):
        #print(S[x:y])
        li.append(S[x:y])

    for i in li:
        print(f'{i}        : {li.count(i)} times')    
    #return li



#print(count_substring('ABCDCDC','CDC'))
print(solution('abaaba'))