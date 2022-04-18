
import random

class Die:
    def __init__(self, sides_count, current_face_value):
        self.sides_count = sides_count
        self.__sides_count = sides_count
        self.current_face_value = current_face_value
        pass
    
    def getCurrentFaceValue(self):
        return self.current_face_value
    
    def setCurrentFaceValue(self, roll):
        self.current_face_value = roll
    
    def displayFaceValue(self):
        print(f"({self.current_face_value})", end=" ")
        
    def roll(self):
        self.setCurrentFaceValue(random.randint(1, self.__sides_count))
        
    def __str__(self):
        return str('\nA rolling die with {0} sides'.format(self.__sides_count))

fourSided = Die(1,0)
active = True
roll_result= []
print(fourSided)
for x in range(5):
    fourSided.roll()
    fourSided.displayFaceValue()
    roll_result.append(fourSided.getCurrentFaceValue())
for roll in roll_result:
    if roll_result[0] != roll:
        active = False
if active == True:
    print(f"\nYahtzee!!!")