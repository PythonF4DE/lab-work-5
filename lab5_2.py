class Fish:
	def __init__(self, name, age, species, size, prefferedFood, isAgressive, neededSpace):
		self.name = name
		self.age = age
		self.species = species
		self.size = size
		self.prefferedFood = prefferedFood
		self.isAgressive = isAgressive
		self.neededSpace = neededSpace

class Aquarium:
	def __init__(self, totalVolume):
		self.totalVolume = totalVolume
		self.freeSpace = totalVolume
		self.listOfFish = []

	def biggestV2(self):
		self.listOfFish.sort(key=lambda fish: fish.size, reverse=True)
		return [fish.name for fish in self.listOfFish[0:3]]
		

	def addFish(self, who):
		if self.freeSpace - who.neededSpace >= 0:
			if len(self.listOfFish) == 0 or self.listOfFish[0].isAgressive == who.isAgressive:
				self.freeSpace -= who.neededSpace
				self.listOfFish.append(who)
				print("Fish has entered aquarium location successfuly!")
			else:
				print("Sorry, agressive fish stays with agresssive only!")
		else:
			print("Sorry, aquarium does not have enough space for this fish!")


whiteShark = Fish("White Shark", 15, "white shark", 50, "meat", True, 25)
bullShark = Fish("Bull Shark", 10, "bull shark", 40, "meat", True, 15)
tigerShark = Fish("Tiger Shark", 10, "tiger shark", 40, "meat", True, 15)
goldfish = Fish("Goldfish", 10, "golden fish", 2, "insects", False, 1)
largemouthBass = Fish("Largemouth Bass", 5, "largemouth bass", 5, "zooplankton", False, 3)
catfish = Fish("Catfish", 5, "catfish", 5, "seeds", False, 3)

def main():
	aqua1 = Aquarium(30)
	aqua1.addFish(whiteShark)
	aqua1.addFish(bullShark)
	aqua1.addFish(goldfish)

	aqua2 = Aquarium(10)
	aqua2.addFish(goldfish)
	aqua2.addFish(largemouthBass)
	print(aqua2.biggestV2())

	aqua3 = Aquarium(1000)
	aqua3.listOfFish.append(whiteShark)
	aqua3.listOfFish.append(goldfish)
	aqua3.listOfFish.append(catfish)
	aqua3.listOfFish.append(tigerShark)
	aqua3.listOfFish.append(bullShark)
	print(aqua3.biggestV2())

main()