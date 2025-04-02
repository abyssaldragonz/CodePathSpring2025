# Week 5 Session 1 Standard Problem Set Version 1

import re
from collections import Counter


# PROBLEM FOUR
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
	
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and not re.fullmatch(r"[A-Za-z\s]+", new_catchphrase): # or " ".join(list(new_catchphrase)).isalpha()
            print("Invalid catchphrase")
        else:
            print("Catchphrase Updated!")
            self.catchphrase = new_catchphrase

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)


# PROBLEM FIVE
    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        for item in valid_items:    # valid
            if item in item_name:
                self.furniture.append(item)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)


# PROBLEM SIX
    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty")
        else:
            count = Counter(self.furniture)
            print(str(count)[9:-2])
            for item, freq in count.items():
                print(item + ": " + str(freq), end=", ")

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()


# PROBLEM SEVEN
def of_personality_type(townies, personality_type):
    retList = []
    for person in townies:
        if person.personality == personality_type:
            retList.append(person.name)
    return retList
    
# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))