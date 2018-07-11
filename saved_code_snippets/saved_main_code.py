prompt = input("Would you like to generate a completely random character? ")

if prompt == "No":
  self.inLevel = int(input("What level is your NPC? "))
  self.inRace = input("What is your NPC's race? Enter their race as a list of the following format: ('race name', '+stat 1 (ex. STR);+stat 2 (ex. DEX);-stat' OR 'ANY')If you would like their race to be random, enter \"rand\" ")
  self.inName = input("What is your NPC's name? If you would like their name to be random, enter \"rand\" ")
  self.inGender = input("What is your NPC's gender? If you would like their gender to be random, enter \"rand\" ")
  self.inStats = input("What are your NPC's stats? Enter their stats as a list of the following format: [STR, DEX, CON, INT, WIS, CHA]\nIf you would like their stats to be random, enter \"rand\" ")
  self.inClass = input("What is your NPC's class? Enter their class as a list of the following format: ['class name', ['most important stat', 'second-most important stat', ... 'least important stat']]\nIf you would like their class to be random, enter \"rand\" ")
  self.inFeats = input("What are your NPC's feats? Enter their feats as a list of the following format: [Feat 1, Feat 2, ...]\nIf you would like their feats to be random, enter \"rand\" ")
  self.inSkills = input("What are your NPC's skills? Enter their skills as a list of the following format: [(Skill 1, Number of Points), (Skill 2, Number of Points), ...]\nIf you would like their skills to be random, enter \"rand\" ")

elif prompt == "Yes":
  self.inLevel = int(input("What level is your NPC? "))
  self.inRace = "rand"
  self.inName = "rand"
  self.inGender = "rand"
  self.inStats = "rand"
  self.inClass = "rand"
  self.inFeats = "rand"
  self.inSkills = "rand"

else:
  print("Please enter \"Yes\" or \"No\".")
  self.get_inputs()
