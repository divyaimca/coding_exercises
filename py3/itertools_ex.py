#https://data-flair.training/blogs/python-itertools-tutorial/


from  itertools import *

for i in count(10,2):
    print(i)
    if i>25: break

for i in count():
    print(i)

for i in cycle(['red','green','blue']):
    print(i)

for i in repeat('Red',3):
    print(i)

for i in product([1,2,3],[4,5,6]):
    print(i)

for i in product('AB','CD','EF'):
    print(i)

for i in product('AB','CD',repeat=2):
    print(i)
for i in permutations('ABCD'):
    print(i)

for i in permutations('ABCD',3):
    print(i)

for i in combinations('ABCD',2):
    print(i)

for i in combinations(range(4),3):
    print(i)

from itertools import combinations_with_replacement as cwr
for i in cwr('ABCD',2):
    print(i)


