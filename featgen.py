import random

def generate(myrace, myclass, mystats, infeats, inlevel):

	if infeats != "rand":
		return infeats

	# elif myclass == "Barbarian":
	# 	#Barbarian strength build
			#Human Bonus Feat) Toughness
			#1) Power Attack
			#3) Improved Initiative
			#5) Endurance
			#7) Diehard
			#9) Improved Critical (main weapon)
			#11) Sickening Critical
			#13) Staggering Critical
			#15) Blinding Critical
			#17) Stunning Critical
			#19) Heroic Defiance
			
		#TO ADD
		#Barbarian archer build
		#Barbarian mounted build
		#Totem barbarian build
		#Invulnerable rager barbarian build (uses Stalwart, tank build)

	# elif myclass == "Bard":

		#TO ADD
		#Bard controller build
		#Bard archer build
		#Bard melee build
	# 	#Bard casting build
		#Bard social build

	# elif myclass == "Cleric":
		#Cleric bruiser build
		#Cleric caster build

	# elif myclass == "Druid":
	# 	#Druid bruiser build
		#Druid archetypes?

	# elif myclass == "Fighter":
	# 	#Fighter 2h build
		#Fighter archery build
		#Fighter mounted build
		#Fighter OHF build
		#Fighter THF build
		#Fighter sword and board build

	# elif myclass == "Monk":
	# 	#Monk unarmed build
		#Monk armed build
		#Monk ranged build
		#Monk switch hitter build

	# elif myclass == "Paladin":
	# 	#Paladin social build
		#Paladin tank build
		#Paladin melee smite build
		#Paladin ranged smite build

	# elif myclass == "Ranger":
	# 	#Ranger archer build
		#Ranger TWF build
		#Ranger switch hitter build

	# elif myclass == "Rogue":
	# 	#Rogue TWF build
		#Rogue social build
		#Rogue THF build
		#Rogue archery build

	# elif myclass == "Sorcerer":
	# 	#Sorcerer utility build
		#Sorcerer blast build
		#Sorcerer mixed build


	# elif myclass == "Wizard":
	# 	#Wizard control build
		#Wizard debuff build
		#Wizard buff build
		#Wizard save or die build
		#Wizard blast build
		#Wizard summoning build

	else:
		return ['Just', 'testing', 'for', 'now!']
		#Account for input classes here, make an educated guess about feats based on stats