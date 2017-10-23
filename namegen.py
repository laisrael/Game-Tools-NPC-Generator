import random

def generate(inname, ingender, myrace):

	#Proof of concept using a list for now, need to find a way to generate
	#names en-masse and either create them on the fly or put a bunch in a DB

	#Also, an androgynous set of names would be nice, but for now just choose
	#randomly between male and female names

	genders = [
	#Weighted to allow for a 1/40 chance of a non-binary NPC, a 20/40 chance
	#of a female NPC, and a 19/40 chance of a male NPC.
			 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male',
			 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female', 'female',
			 'non-binary']
	if ingender == 'rand':
		mygender = random.choice(genders)
	else:
		mygender = ingender
	
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

	if inname == 'rand':
		#Needs to be changed to pick correct racial/gender names
		if myrace == 'human':
			if mygender == 'male':
				myname = random.choice(humanMales)
			elif mygender == 'female':
				myname = random.choice(humanFemales)
			else:
				myname = random.choice((humanMales + humanFemales))
		elif myrace == 'halfling':
			if mygender == 'male':
				myname = random.choice(halflingMales)
			elif mygender == 'female':
				myname = random.choice(halflingFemales)
			else:
				myname = random.choice(halflingMales + halflingFemales)
		elif myrace == 'half-orc':
			if mygender == 'male':
				myname = random.choice(halforcMales)
			elif mygender == 'female':
				myname = random.choice(halforcFemales)
			else:
				myname = random.choice(halforcMales + halforcFemales)
		elif myrace == 'half-elf':
			if mygender == 'male':
				myname = random.choice(halfelfMales)
			elif mygender == 'female':
				myname = random.choice(halfelfFemales)
			else:
				myname = random.choice(halfelfMales + halfelfFemales)
		elif myrace == 'gnome':
			if mygender == 'male':
				myname = random.choice(gnomeMales)
			elif mygender == 'female':
				myname = random.choice(gnomeFemales)
			else:
				myname = random.choice(gnomeMales + gnomeFemales)
		elif myrace == 'elf':
			if mygender == 'male':
				myname = random.choice(elfMales)
			elif mygender == 'female':
				myname = random.choice(elfFemales)
			else:
				myname = random.choice(elfMales + elfFemales)
		elif myrace == 'dwarf':
			if mygender == 'male':
				myname = random.choice(dwarfMales)
			elif mygender == 'female':
				myname = random.choice(dwarfFemales)
			else:
				myname = random.choice(dwarfMales + dwarfFemales)
		else:
			myname = random.choice(humanMales + humanFemales + halfingMales + halflingFemales + halforcMales + halforcFemales + halfelfMales + halfelfFemales + gnomeMales + gnomeFemales + elfMales + elfFemales + dwarfMales + dwarfFemales)
	else:
		myname = inname
	return (myname, mygender)