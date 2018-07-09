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

class Race():
    def __init__(self, inRace):
        if inRace == "rand":
            #Classes are returned with a list of stats in order of where they will allocate stat points, from highest to lowest.
            self.finalRace, self.raceStats = random.choice(races)
        else:
            self.finalRace, self.raceStats = inRace

    def generate(self):
        return (self.finalRace, self.raceStats)
