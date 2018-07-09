import random

humanMales = ['Kharmat', 'Dalba', 'Tegvith Palewolf', 'Sunfrarg Windlash', 'Kornik Distant', 'Borne Ukiddr', 'Sirliam Iggo', 'Hellmem Vusha', 'Jurut Shamikh', 'Were Samam', 'Unkheif Meizghar', 'Sinkhau Suhif']
humanFemales = ['Vurnan', 'Ulbuh', 'Fodfa Freeeyes', 'Thaulka Frostbrace', 'Kerho Dasteg', 'Haldo Klaenoddr', 'Shuggast Isse', 'Neafe Hiknem', 'Ghethih Vruzilm', 'Share Bhalme', 'Shibe Utenn', 'Sunke Maqish']

halflingMales = ['Bok Duskdream', 'Vrek Selnailk', 'Brol Evenless', 'Reldaar Urwedlolk', 'Naful Nightbrace', 'Briri Vugne', 'Doldord Longworth', 'Nuldevam Cialnalk', 'Xorifar Autumnworth', 'Davudal Glibblugnurd']
halflingFemales = ['Filran Longworth', 'Lazi Nenvird', 'Wisoth Flatless', 'Inoe Ilvasba', 'Hufe Honorsong', 'Valrorli Ulmuth', 'Jiuziahne Mossvale', 'Jothaeyih Gneandig', 'Prelalke Orbsoar', 'Enevi Glingabblith']

halforcMales = ['Bras Hetsky', 'Bun Katrotsky', 'Pix Bum', 'Drer Thadkexne', 'Hrolm Beshky', 'Giakholm Doglar', 'Cralkraich Wam', 'Grudu Ulgrok', 'Adron Taz', 'Tsozrozvelm Estetkor']
halforcFemales = ['Nolluh Haz', 'Once Shilrashky', 'Woslu Jeld', 'Islo Wedutruv', 'Civai Shelm', 'Cozrou Endrin', 'Omga Gnim', 'Burde Conrad', 'Goudribon Wek', 'Bragladeh Akirrod']

halfelfMales = ['Dann Zodoho', 'Kuk Traw', 'Ruh Prumirtal', 'Nistral Dagweaw', 'Perdok Drusgedur', 'Terlann Krart', 'Emos Orlalyior', 'Kherdusvru Murks', 'Binvrurvryn Sujilgath', 'Zunisul Ossraw']
halfelfFemales = ['Tuass Prearume', 'Shie Ful', 'Son Kirrigond', 'Chourya Gresos', 'Thrinde Fatreireind', 'Reldin Bam', 'Zhiclulves Kledimren', 'Cheyuaswu Kreenn', 'Cherruyo Krolardor', 'Zhugneye Yigguw']

gnomeMales = ['Hierd Nerndillocks', 'Hur Freess', 'Qord Suzluonco', 'Kopat Opli', 'Eshmoust Noclattlar', 'Shmubra Gloh', 'Ozzed Thuttlepraack', 'Cizzadqa Vest', 'Hokrunqu Adlonson', 'Zamzobruzzed Tiwack']
gnomeFemales = ['Fick Kleglocneng', 'Gos Feb', 'Zut Fritlucog', 'Pesh Rulpiss', 'Genzeth Kluasnuncoo', 'Adock Jid', 'Fagnom Maaluvreg', 'Trixiznueg Sud', 'Gaveterlug Teeplum']

elfMales = ['Koss Kadnenin', 'Vul Grah', 'Sian Helugih', 'Halvran Thonnon', 'Zumvan Yulvimvu', 'Thiga Tah', 'Elies Theyissin', 'Domunan Feh', 'Coriogres Seigohhih', 'Neironthalmas Komrol']
elfFemales = ['Meclo Monnares', 'Phogo Zhun', 'Pharvas Wilvrutha', 'Inthe Shaniol', 'Mucullas Munsamri', 'Tulyalmaess Con', 'Thovumea Zioyelsum', 'Tovaha Thuh', 'Siagiaroma Jelliuh', 'Fohanici Fallis']

dwarfMales = ['Brels Ironpelt', 'Trag Mavuls', 'Or Fistbrand', 'Rold Jes', 'Boc Firebash', 'Srunfurd Kazmog', 'Strokod Wildblaze', 'Evols Grakkall', 'Feklug Stormshade', 'Daindryk Ghuck']
dwarfFemales = ['Khum Moltenpunch', 'Ye Byklud', 'So Deeppunch', 'Tim Beth', 'Ra Coldgem', 'Ghulgwas Ghamryd', 'Kivull Stoneflow', 'Ongu Bryngodd', 'Nuddal Embersurge', 'Gevlir Srob']

genders = [
#Weighted to allow for a 1/40 chance of a non-binary NPC, a 20/40 chance
#of a female NPC, and a 19/40 chance of a male NPC.

		 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male',
		 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female',
		 'non-binary']

#Proof of concept using a list for now, need to find a way to generate
#names en-masse and either create them on the fly or put a bunch in a DB

#Also, an androgynous set of names would be nice, but for now just choose
#randomly between male and female names

class Name():
	def __init__(self, inName, inGender, finalRace):
		self.finalName = inName
		self.finalGender = inGender
		self.finalRace = finalRace

	def get_gender(self):
		if self.finalGender == 'rand':
			self.finalGender = random.choice(genders)

	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(humanMales + halfingMales +  halforcMales + halfelfMales + gnomeMales + elfMales + dwarfMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(humanFemales + halflingFemales + halforcFemales + halfelfFemales + gnomeFemales + elfFemales + dwarfFemales)
		else:
			self.finalName = random.choice(humanMales + humanFemales + halfingMales + halflingFemales + halforcMales + halforcFemales + halfelfMales + halfelfFemales + gnomeMales + gnomeFemales + elfMales + elfFemales + dwarfMales + dwarfFemales)

	def generate(self):
		self.get_gender()
		self.get_name()

		return (self.finalName, self.finalGender)

class HumanName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(humanMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(humanFemales)
		else:
			self.finalName = random.choice((humanMales + humanFemales))

class HalflingName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(halflingMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(halflingFemales)
		else:
			self.finalName = random.choice(halflingMales + halflingFemales)

class HalfOrcName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(halforcMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(halforcFemales)
		else:
			self.finalName = random.choice(halforcMales + halforcFemales)

class HalfElfName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(HalfElfMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(halfelfFemales)
		else:
			self.finalName = random.choice(halfelfMales + halfelfFemales)

class GnomeName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(gnomeMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(gnomeFemales)
		else:
			self.finalName = random.choice(gnomeMales + gnomeFemales)

class ElfName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(elfMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(elfFemales)
		else:
			self.finalName = random.choice(elfMales + elfFemales)

class DwarfName(Name):
	def get_name(self):
		if self.finalName != 'rand':
			pass
		elif self.finalGender == 'male':
			self.finalName = random.choice(dwarfMales)
		elif self.finalGender == 'female':
			self.finalName = random.choice(dwarfFemales)
		else:
			self.finalName = random.choice(dwarfMales + dwarfFemales)
