import random

classes = [
    ('Barbarian', ['STR', 'CON', 'DEX', 'WIS', 'CHA', 'INT']),
    ('Bard', ['CHA', 'CON', 'STR', 'DEX', 'WIS', 'INT']),
    ('Cleric', ['WIS', 'CHA', 'CON', 'DEX', 'INT', 'STR']),
    ('Druid', ['WIS', 'CON', 'STR', 'DEX', 'INT', 'CHA']),
    ('Fighter', ['STR', 'CON', 'DEX', 'WIS', 'INT', 'CHA']),
    ('Monk', ['STR', 'WIS', 'CON', 'DEX', 'INT', 'CHA']),
    ('Paladin', ['CHA', 'WIS', 'STR', 'CON', 'DEX', 'INT']),
    ('Ranger', ['STR', 'DEX', 'WIS', 'CHA', 'CON', 'INT']),
    ('Rogue', ['DEX', 'CHA', 'CON', 'WIS', 'INT', 'STR']),
    ('Sorcerer', ['CHA', 'DEX', 'CON', 'WIS', 'INT', 'STR']),
    ('Wizard', ['INT', 'CON', 'DEX', 'WIS', 'CHA', 'STR'])
    ]

class Class():
    def __init__(self, inClass):
        if inClass == "rand":
            #Classes are returned with a list of stats in order of where they will allocate stat points, from highest to lowest.
            self.finalClass, self.statPref = random.choice(classes)
        else:
            self.finalClass, self.statPref = inClass

    def generate(self):
        return (self.finalClass, self.statPref)
