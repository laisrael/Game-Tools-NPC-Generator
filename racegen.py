import random

#Implement separate lists for the core races vs. special races
races = ["Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human"]

def generate(inrace):
	if inrace == "rand":
		race = random.choice(races)
	else:
		#Currently only supports Core Races
		race = inrace
	return race