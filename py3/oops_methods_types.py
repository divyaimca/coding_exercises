class PlayerMethods:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    
    def instanceMethod(self):
        print(f'Hello world {self.name} from instanceMethod type')
        return 'done'

    
    @staticmethod
    def staticMethod(num1, num2):
        print('Hello World from static method Type')
        return num1 * num2

    @classmethod
    def classMethod(cls, num1, num2):
        print(f'Hello world  from class method type')
        cls.staticMethod(num1, num2)
        print(num1 + num2)
        return cls('anji',num1 + num2)

obj1 = PlayerMethods('manan',35)


print(obj1.instanceMethod())
print(PlayerMethods.staticMethod(2,5))
#print(PlayerMethods.classMethod(5,10))
obj2 = PlayerMethods.classMethod(6,7)
print(obj2)