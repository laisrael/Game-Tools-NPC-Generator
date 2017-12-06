import random

def generate(myrace, myclass, mystats, infeats, inlevel):

	if infeats != "rand":
		return infeats

	# elif myclass == "Barbarian":
	# 	#Barbarian strength build

		#TO ADD
		#Barbarian archer build
		#Barbarian mounted build
		#Totem barbarian build

	# elif myclass == "Bard":
	# 	#Bard casting build

	# elif myclass == "Cleric":
	# 	#Cleric bruiser build

	# elif myclass == "Druid":
	# 	#Druid bruiser build

	# elif myclass == "Fighter":
	# 	#Fighter melee strength build

	# elif myclass == "Monk":
	# 	#Monk melee strength build

	# elif myclass == "Paladin":
	# 	#Paladin bruiser build

	# elif myclass == "Ranger":
	# 	#Ranger strength build

	# elif myclass == "Rogue":
	# 	#Rogue Dexterity assassin build

	# elif myclass == "Sorcerer":
	# 	#Sorcerer squishy control mage build

	# elif myclass == "Wizard":
	# 	#Wizard squishy control mage build

	else:
		return ['Just', 'testing', 'for', 'now!']
		#Account for input classes here, make an educated guess about feats based on stats