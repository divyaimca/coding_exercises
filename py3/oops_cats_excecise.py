#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('anji',5)
cat2 = Cat('pooji',6)
cat3 = Cat('kanki',7)


# 2 Create a function that finds the oldest cat
def oldestCat(*ages):
    return max(ages)




# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2print(f' Oldest cat is {oldestCat(cat1.age,cat2.age,cat3.age)} years old')
print(f' Oldest cat is {oldestCat(cat1.age,cat2.age,cat3.age)} years old')
