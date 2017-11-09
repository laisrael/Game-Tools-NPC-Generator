import random

def generate(instats, inlevel, racestats, statpref):
	#Should this take into account classes that don't want to dump all their stat points in one stat?

	#GENERATION

	#Randomly generate stat numbers

	statNums = []
	finalStats = []
	i = 0
	while i < 6:
		diceRolled = 0
		finalDice = 0
		#Roll 4d6 and drop the lowest
		die_1 = random.randint(1, 6)
		die_2 = random.randint(1, 6)
		die_3 = random.randint(1, 6)
		die_4 = random.randint(1, 6)
		dieList = [die_1, die_2, die_3, die_4]
		dieList.remove(min(dieList))
		for die in dieList:
			finalDice += die
		diceRolled += 1
		statNums.append(finalDice)
		i += 1

	statNums.sort(reverse = True)

	for num in statNums:
		finalStats.append([num, statpref[0]])
		statpref.remove(statpref[0])

	#BONUSES

	#Assign racial modifiers

	if racestats == "ANY":
		finalStats[0][0] += 2
	else:
		raceStatChanges = racestats.split(';')
		for stat in raceStatChanges:
			if stat[0] == "+":
				changedStat = stat[1:]
				for finalStat in finalStats:
					if finalStat[1] == changedStat:
						finalStat[0] += 2
			else:
				changedStat = stat[1:]
				for finalStat in finalStats:
					if finalStat[1] == changedStat:
						finalStat[0] -= 2				


	#Assign level bonuses

	abilityBonus = inlevel // 4
	finalStats[0][0] += abilityBonus

	return finalStats