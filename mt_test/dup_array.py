def findDup(li):
    print(li)
    dup = [x for x in set(li) if li.count(x) > 1]
    return dup




print(findDup([2,3,1,2,3]))