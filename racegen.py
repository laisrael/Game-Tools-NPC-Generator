import random

races = [("Dwarf", "+CON;+WIS;-CHA"), ("Elf", "+DEX;+INT;-CON"), ("Gnome", "+CON;+CHA;-STR"), ("Half-Elf", "ANY"), ("Half-Orc", "ANY"), ("Halfling", "+DEX;+CHA;-STR"), ("Human", "ANY")]

class Race():
    def __init__(self, inRace):
        if inRace == "rand":
            self.finalRace, self.raceStats = random.choice(races)
        else:
            self.finalRace, self.raceStats = inRace

    def generate(self):
        return (self.finalRace, self.raceStats)
