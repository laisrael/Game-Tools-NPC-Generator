import random

def generate(inclass):
    #Using core classes only for proof of concept
    #Does not account for the flexibility between STR/DEX choices
    if inclass != "rand":
        return inclass
    else:
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
        return random.choice(classes)