import random

class Die():
	def __init__(self):
		self.currentValue = 0

	def roll(self):
		self.currentValue = random.randint(1, 6)

	def get_value(self):
		return self.currentValue

class DieList():
	def __init__(self):
		self.dieList = []
		self.summedDice = 0

	def roll_dice(self):
		i = 0

		while i < 4:
			die = Die()
			die.roll()
			self.dieList.append(die.get_value())
			i += 1

	def drop_lowest(self):
		self.dieList.remove(min(self.dieList))

	def sum_dice(self):
		for die in self.dieList:
			self.summedDice += die

	def get_summedDice(self):
		return self.summedDice

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
		i = 0

		while i < 6:
			stat = DieList()
			stat.roll_dice()
			stat.drop_lowest()
			stat.sum_dice()
			stat = stat.get_summedDice()
			self.rolledDice.append(stat)
			i += 1

		self.rolledDice.sort(reverse = True)

	def set_finalStats(self):
		for num in self.rolledDice:
			self.finalStats.append([num, self.statPref[0]])
			self.statPref.remove(self.statPref[0])

	def apply_racialModifiers(self):
		if self.raceStats == "ANY":
			self.finalStats[0][0] += 2

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
		self.abilityBonus = self.inLevel // 4
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
