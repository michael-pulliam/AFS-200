class Dog:
        def __init__(self, name, breed, age, color, size):
            self.name = name
            self.breed = breed
            self.age = age
            self.color = color
            self.size = size
            
        def bark(self):
            print("Woof..Woof")
            
        def getName(self):
            return self.name
            
        def setName(self, name):
            self.name = name
            
        def getAge(self):
            return self.age
            
        def setAge(self,age):
            self.age = age