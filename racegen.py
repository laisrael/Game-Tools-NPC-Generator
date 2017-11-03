import random

#Implement separate lists for the core races vs. special races
races = [("Dwarf", "+2 CON;+2 WIS;-2 CHA"), ("Elf", "+2 DEX;+2 INT;-2 CON"), ("Gnome", "+2 CON;+2 CHA;-2 STR"), ("Half-Elf", "ANY"), ("Half-Orc", "ANY"), ("Halfling", "+2 DEX;+2 CHA;-2 STR"), ("Human", "ANY")]

def generate(inrace):
	if inrace == "rand":
		race = random.choice(races)
	else:
		#Currently only supports Core Races
		race = inrace
	return race