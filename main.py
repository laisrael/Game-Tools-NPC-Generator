import racegen, namegen, statgen, classgen, featgen, skillgen

class NPC():
	def __init__(self):
		#Inputs
		self.inLevel = None
		self.inRace = None
		self.inName = None
		self.inGender = None
		self.inStats = None
		self.inClass = None
		self.inFeats = None
		self.inSkills = None

		#Intermediate values
		self.raceStats = None
		self.statPref = None

		#Outputs
		self.finalLevel = None
		self.finalRace = None
		self.finalName = None
		self.finalGender = None
		self.finalStats = None
		self.finalClass = None
		self.finalFeats = None
		self.finalSkills = None

	def get_inputs(self):
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

	def gen_race(self):
		race = racegen.Race(self.inRace)
		self.finalRace, self.raceStats = race.generate()

	def gen_name(self):
		if self.finalRace == "Human":
			name = namegen.HumanName(self.inName, self.inGender, self.finalRace)

		elif self.finalRace == "Halfling":
			name = namegen.HalflingName(self.inName, self.inGender, self.finalRace)

		elif self.finalRace == "Half-Orc":
			name = namegen.HalfOrcName(self.inName, self.inGender, self.finalRace)

		elif self.finalRace == "Half-Elf":
			name = namegen.HalfElfName(self.inName, self.inGender, self.finalRace)

		elif self.finalRace == "Gnome":
			name = namegen.GnomeName(self.inName, self.inGender, self.finalRace)

		elif self.finalRace == "Elf":
			name = namegen.ElfName(self.inName, self.inGender, self.finalRace)

		elif self.finalRace == "Dwarf":
			name = namegen.DwarfName(self.inName, self.inGender, self.finalRace)

		else:
			name = namegen.Name(self.inName, self.inGender, self.finalRace)

		self.finalName, self.finalGender = name.generate()

	def gen_class(self):
		myclass = classgen.Class(self.inClass)
		self.finalClass, self.statPref = myclass.generate()

	def gen_stats(self):
		stats = statgen.Stats(self.inStats, self.inLevel, self.raceStats, self.statPref)
		self.finalStats = stats.generate()

	def gen_feats(self):
		self.finalFeats = featgen.generate(self.finalRace, self.finalClass, self.finalStats, self.inFeats, self.inLevel)

	def gen_skills(self):
		self.finalSkills = skillgen.generate(self.finalStats, self.finalClass, self.inSkills)

	def print_npc(self):
		print("Your NPC's race is: " + self.finalRace)
		print("Your NPC's name is: " + self.finalName)
		print("Your NPC's gender is: " + self.finalGender.title())
		print("Your NPC's class is: " + self.finalClass)
		print("Your NPC's stats are: " + str(self.finalStats))
		print("Your NPC's feats are: " + str(self.finalFeats))
		print("Your NPC's skills are: " + self.finalSkills)

	def create(self):
		self.get_inputs()
		self.gen_race()
		self.gen_name()
		self.gen_class()
		self.gen_stats()
		self.gen_feats()
		self.gen_skills()
		self.print_npc()

npc = NPC()
npc.create()
