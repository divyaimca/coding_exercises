from  random import *

class GuessingGame():

    def __init__(self, rand_choice=randint(0,10)):
        self.rand_choice = rand_choice

    def reset_random(self):
        print('Resetting Random Choice')
        self.rand_choice = randint(0,10)

    def guess(self):
        num = int(input('Please input your guess (0-10): '))
        if num == self.rand_choice:
            print('Correct Guess!') 
        elif num > self.rand_choice:
            print('Sorry you didn\'t guess correctly!')
            print('Guess Lower')
            print('Call the guess() method again to try again.')
        else:
            print('Sorry you didn\'t guess correctly!')
            print('Guess Higher')
            print('Call the guess() method again to try again.')


g = GuessingGame()
print(g.rand_choice)
g.reset_random()
print(g.rand_choice)
g.guess()

