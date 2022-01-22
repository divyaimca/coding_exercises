class PlayerChracter:
    ##Class object attribute
    # membership = True
    # def __init__(self, name, age):   ## initialized with self, self is the object name tho which the class is asisgned e.g object1, pbject2
    #     if(PlayerChracter.membership): ## Check if membership is True continue with game playing
    #         self.name = name   ### Attributes or Properties of the class
    #         self.age = age


    def __init__(self, name='anonymous', age=0):   
        if(age >= 18): ## Check if membership is True continue with game playing
            self.name = name   ### Attributes or Properties of the class
            self.age = age
        

    def sayHello(self):             ## Method defined
        print(f'Hello your name is {self.name}')
        return 'done'


    def run(self):
        print('run')
        return 'done'

# player1 = PlayerChracter('Anji',26)
# player2 = PlayerChracter('Puji',30)
# print(player1.membership)
# print(player1.sayHello())
# print(player1.run())
# print(player2.name)
# print(player1.age)

#help(PlayerChracter)

player1 = PlayerChracter('pk',17)   ### object wll not instantiate as the age is below 18 as defined in __init__ methods
player2 = PlayerChracter('pk1',18)
print(player1.age)
print(player2.name)



