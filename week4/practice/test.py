
import random

class Rolling_Die:
    
    def __init__(self, sides_count):
        self.sides_count = sides_count
        self.__sides_count = sides_count
        pass
    
    # def getCurrentFaceValue(self):
    #     return self.__sides_count
    
    def roll(self):
        return random.randint(1, self.__sides_count)
    
    # def showDieFace(self):
    #     return 
    def check_yatzy(self, dice_list):
        if len(set(dice_list)) == 1:
            return True
        return False
    
    def __str__(self):
        return str("\nA rolling die with {0} sides".format(self.__sides_count))
    
# Rolls the 6-sided die
fourSided = Rolling_Die(4)

print(fourSided)
for _ in range(5):
    print(fourSided.roll(), end=" ")
    print (f'is it Yatzy? {fourSided.check_yatzy()}')
    
input()


# sixSided = Rolling_Die(6)
# eightSided = Rolling_Die(8)
# tenSided = Rolling_Die(10)
# twentySided = Rolling_Die(20)
# oneHundredSided = Rolling_Die(100)

# print(sixSided)
# for _ in range(5):
#     print(sixSided.roll(), end=" ")
   
# print(eightSided)
# for _ in range(5):
#     print(eightSided.roll(), end=" ") 