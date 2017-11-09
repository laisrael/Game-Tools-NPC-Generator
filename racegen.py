import random

#Implement separate lists for the core races vs. special races
races = [("Dwarf", "+CON;+WIS;-CHA"), ("Elf", "+DEX;+INT;-CON"), ("Gnome", "+CON;+CHA;-STR"), ("Half-Elf", "ANY"), ("Half-Orc", "ANY"), ("Halfling", "+DEX;+CHA;-STR"), ("Human", "ANY")]

def generate(inrace):
	if inrace == "rand":
		race = random.choice(races)
	else:
		#Currently only supports Core Races
		race = inrace
	return race