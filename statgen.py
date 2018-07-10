import random

class Die():
	def __init__(self, currentValue):
		self.currentValue = 0

	def roll(self):
		self.currentValue = random.randint(1, 6)

	def get_value(self):
		return self.currentValue

class DieList():
	def __init__(self, dieList):
		self.dieList = [0, 0, 0, 0]

	def roll_dice(self):
		die_1 = Die()
		die_1.roll()
		die_2 = Die()
		die_2.roll()
		die_3 = Die()
		die_3.roll()
		die_4 = Die()
		die_4.roll()

		self.dieList[0] = die_1.get_value()
		self.dieList[1] = die_2.get_value()
		self.dieList[2] = die_3.get_value()
		self.dieList[3] = die_4.get_value()

	def drop_lowest(self):
		self.dieList.remove(min(self.dieList))

	def get_dieList(self):
		return self.dieList

class Stats():
	def __init__(self, inStats, inLevel, raceStats, statPref):
		self.inStats = inStats
		self.inLevel = inLevel
		self.raceStats = raceStats
		self.statPref = statPref
		self.rolledDice = []
		self.finalStats = []
		self.abilityBonus = 0

	def set_rolledDice(self):
			stat_1 = DieList()
			stat_1.roll_dice()
			stat_1.drop_lowest()

			stat_2 = DieList()
			stat_2.roll_dice()
			stat_2.drop_lowest()

			stat_3 = DieList()
			stat_3.roll_dice()
			stat_3.drop_lowest()

			stat_4 = DieList()
			stat_4.roll_dice()
			stat_4.drop_lowest()

			stat_5 = DieList()
			stat_5.roll_dice()
			stat_5.drop_lowest()

			stat_6 = DieList()
			stat_6.roll_dice()
			stat_6.drop_lowest()

			self.rolledDice.append(stat_1)
			self.rolledDice.append(stat_2)
			self.rolledDice.append(stat_3)
			self.rolledDice.append(stat_4)
			self.rolledDice.append(stat_5)
			self.rolledDice.append(stat_6)

			self.rolledDice.sort(reverse = True)

	def set_finalStats(self):
		for num in self.rolledDice:
			self.finalStats.append([num, self.statPref[0]])
			self.statPref.remove(statpref[0])

	def apply_racialModifiers(self):
		if racestats == "ANY":
			finalStats[0][0] += 2
		else:
			#Using nested for loops since races only have up to three stat changes
			self.raceStats = self.raceStats.split(';')
			for stat in self.raceStats:
				if stat[0] == "+":
					changedStat = stat[1:]
					for stat in self.finalStats:
						if stat[1] == changedStat:
							stat[0] += 2
				else:
					changedStat = stat[1:]
					for stat in self.finalStats:
						if stat[1] == changedStat:
							stat[0] -= 2

	def apply_levelModifiers(self):
		self.abilityBonus = self.inlevel // 4
		self.finalStats[0][0] += self.abilityBonus

	def generate(self):
		if self.inStats != "rand":
			return self.inStats
		else:
			self.set_rolledDice()
			self.set_finalStats()
			self.apply_racialModifiers()
			self.apply_levelModifiers()
			return self.finalStats

def generate(instats, inlevel, racestats, statpref):

	if instats != "rand":
		return instats

	else:
		#Should this take into account classes that don't want to dump all their stat points in one stat?

		#GENERATION

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
