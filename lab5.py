"""Code for lab work 5 from programming course"""
class Fish:
    """This class creates a simple object fish that has some parameters"""
    def __init__(self, name, size, is_agressive, needed_space):
        self.name = name
        self.size = size
        self.is_agressive = is_agressive
        self.needed_space = needed_space


class Aquarium:
    """This class creates an object called aquarium for putting fish in it"""
    def __init__(self, total_volume):
        self.total_volume = total_volume
        self.free_space = total_volume
        self.list_of_fish = []

    def get_biggest_fish(self):
        """This method returns a list of 3 biggest fish in aquarium"""
        self.list_of_fish.sort(key=lambda fish: fish.size, reverse=True)
        return [fish.name for fish in self.list_of_fish[0:3]]

    def add_fish(self, who):
        """This method adds fish to aquarium if all conditions are met"""
        if self.free_space - who.needed_space >= 0:
            if len(self.list_of_fish) == 0 or self.list_of_fish[0].is_agressive == who.is_agressive:
                self.free_space -= who.needed_space
                self.list_of_fish.append(who)
                return "Fish has entered aquarium location successfuly!"
            return "Sorry, agressive fish stays with agressive only!"
        return "Sorry, aquarium does not have enough space for this fish!"


white_shark = Fish("White Shark", 15, True, 50)
bull_shark = Fish("Bull Shark", 10, True, 40)
tiger_shark = Fish("Tiger Shark", 10, True, 40)
blue_shark = Fish("Blue Shark", 12, True, 35)
pirania = Fish("Pirania", 3, True, 5)
kraken = Fish("Kraken", 100, True, 150)
goldfish = Fish("Goldfish", 1, False, 2)
largemouth_bass = Fish("Largemouth Bass", 5, False, 5)
catfish = Fish("Catfish", 5, False, 5)


def main():
    """This function runs the app"""
    home_aqua = Aquarium(30)
    home_aqua.add_fish(white_shark)
    home_aqua.add_fish(bull_shark)
    home_aqua.add_fish(goldfish)
    print(home_aqua.get_biggest_fish())

    zoo_aqua = Aquarium(10)
    zoo_aqua.add_fish(goldfish)
    zoo_aqua.add_fish(largemouth_bass)
    print(zoo_aqua.get_biggest_fish())

    ocean = Aquarium(1000)
    ocean.add_fish(white_shark)
    ocean.add_fish(pirania)
    ocean.add_fish(blue_shark)
    ocean.add_fish(tiger_shark)
    ocean.add_fish(bull_shark)
    ocean.add_fish(kraken)
    print(ocean.get_biggest_fish())


main()
