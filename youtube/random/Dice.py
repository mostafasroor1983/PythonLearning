import random
class Dice:    
    def roll(self):
        n1 = random.randint(1,6)
        n2 = random.randint(1,6)
        return n1, n2 # return a locked tuple
    
dice = Dice()
print(dice.roll())
