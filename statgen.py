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
		self.dieList = [0, 0, 0, 0]
		self.summedDice = 0

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

	def add_dice(self):
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
			stat_1 = DieList()
			stat_1.roll_dice()
			stat_1.drop_lowest()
			stat_1.add_dice()
			stat_1 = stat_1.get_summedDice()

			stat_2 = DieList()
			stat_2.roll_dice()
			stat_2.drop_lowest()
			stat_2.add_dice()
			stat_2 = stat_2.get_summedDice()

			stat_3 = DieList()
			stat_3.roll_dice()
			stat_3.drop_lowest()
			stat_3.add_dice()
			stat_3 = stat_3.get_summedDice()

			stat_4 = DieList()
			stat_4.roll_dice()
			stat_4.drop_lowest()
			stat_4.add_dice()
			stat_4 = stat_4.get_summedDice()

			stat_5 = DieList()
			stat_5.roll_dice()
			stat_5.drop_lowest()
			stat_5.add_dice()
			stat_5 = stat_5.get_summedDice()

			stat_6 = DieList()
			stat_6.roll_dice()
			stat_6.drop_lowest()
			stat_6.add_dice()
			stat_6 = stat_6.get_summedDice()

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
			
