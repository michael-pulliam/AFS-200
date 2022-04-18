class FarmAnimal:
	def __init__(self,location,numLegs,sound="..."):
		self.location = location
		self.numLegs = numLegs
		self.sound = sound
		
	def getLocation(self):
		return self.location
		
	def make_sound(self):
		print("...")

class Cow(FarmAnimal):  # Is A FarmAnimal
	def __init__(self,location,numLegs,tagID):
		FarmAnimal.__init__(self,location,numLegs,"Moo")
		self.tagID = tagID
	
	def milk(self):
		print("You got milk!")
		
	def make_sound(self):
		print(self.sound)

	def get_sound(self):
		return self.sound

class Horse(FarmAnimal):
	def __init__(self,location,numLegs,breed):
		FarmAnimal.__init__(self,location,numLegs,"Nay")
		self.breed = breed
				
	def make_sound(self):
		print(self.sound)

	def get_sound(self):
		return self.sound
		
	def ride(self):
		print("Giddy Up")      
  
class Chicken(FarmAnimal):
	def __init__(self,location,numLegs,gender):
		if (gender == "male"):
			FarmAnimal.__init__(self,location,numLegs,"Cock-a-doodle-doo")
		else:
			FarmAnimal.__init__(self,location,numLegs,"Cluck")
		self.gender = gender
		
	def make_sound(self):
		print(self.sound)

	def get_sound(self):
		return self.sound

myCow = Cow("Barn",4,"EF-738")
myHorse = Horse("Stable",4,"Mustang")
myHen =	Chicken("Hen House",2,"female")
myRooster = Chicken("Yard",2,"male")   

myFarm = [myCow, myHorse, myHen,myRooster]

for animal in myFarm:

    print("Old MACDONALD had a farm E-I-E-I-O.")
    print("And on his farm he had a cow, E-I-E-I-O.")
    print("With a "+animal.get_sound()+" "+animal.get_sound()+" here")
    print("And a "+animal.get_sound()+" "+animal.get_sound()+" there.")
    print("Here a "+animal.get_sound()+", there a "+animal.get_sound())
    print("Everywhere a "+animal.get_sound()+" "+animal.get_sound())
    print("Old MacDonald had a farm E-I-E-I-O")