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
	gender = random.choice(genders)
	names = [
			 #human males 
			 'Kharmat', 'Dalba', 'Tegvith Palewolf', 'Sunfrarg Windlash', 'Kornik Distant', 'Borne Ukiddr', 'Sirliam Iggo', 'Hellmem Vusha', 'Jurut Shamikh', 'Were Samam', 'Unkheif Meizghar', 'Sinkhau Suhif',
			 #human females
			 'Vurnan', 'Ulbuh', 'Fodfa Freeeyes', 'Thaulka Frostbrace', 'Kerho Dasteg', 'Haldo Klaenoddr', 'Shuggast Isse', 'Neafe Hiknem', 'Ghethih Vruzilm', 'Share Bhalme', 'Shibe Utenn', 'Sunke Maqish',
			 #halfling males
			 'Bok Duskdream', 'Vrek Selnailk', 'Brol Evenless', 'Reldaar Urwedlolk', 'Naful Nightbrace', 'Briri Vugne', 'Doldord Longworth', 'Nuldevam Cialnalk', 'Xorifar Autumnworth', 'Davudal Glibblugnurd',
			 #halfling females
			 'Filran Longworth', 'Lazi Nenvird', 'Wisoth Flatless', 'Inoe Ilvasba', 'Hufe Honorsong', 'Valrorli Ulmuth', 'Jiuziahne Mossvale', 'Jothaeyih Gneandig', 'Prelalke Orbsoar', 'Enevi Glingabblith',
			 #half-orc males
			 'Bras Hetsky', 'Bun Katrotsky', 'Pix Bum', 'Drer Thadkexne', 'Hrolm Beshky', 'Giakholm Doglar', 'Cralkraich Wam', 'Grudu Ulgrok', 'Adron Taz', 'Tsozrozvelm Estetkor',
			 #half-orc females
			 'Nolluh Haz', 'Once Shilrashky', 'Woslu Jeld', 'Islo Wedutruv', 'Civai Shelm', 'Cozrou Endrin', 'Omga Gnim', 'Burde Conrad', 'Goudribon Wek', 'Bragladeh Akirrod',
			 #half-elf males
			 'Dann Zodoho', 'Kuk Traw', 'Ruh Prumirtal', 'Nistral Dagweaw', 'Perdok Drusgedur', 'Terlann Krart', 'Emos Orlalyior', 'Kherdusvru Murks', 'Binvrurvryn Sujilgath', 'Zunisul Ossraw',
			 #half-elf females
			 'Tuass Prearume', 'Shie Ful', 'Son Kirrigond', 'Chourya Gresos', 'Thrinde Fatreireind', 'Reldin Bam', 'Zhiclulves Kledimren', 'Cheyuaswu Kreenn', 'Cherruyo Krolardor', 'Zhugneye Yigguw',
			 #gnome males
			 'Hierd Nerndillocks', 'Hur Freess', 'Qord Suzluonco', 'Kopat Opli', 'Eshmoust Noclattlar', 'Shmubra Gloh', 'Ozzed Thuttlepraack', 'Cizzadqa Vest', 'Hokrunqu Adlonson', 'Zamzobruzzed Tiwack',
			 #gnome females
			 'Fick Kleglocneng', 'Gos Feb', 'Zut Fritlucog', 'Pesh Rulpiss', 'Genzeth Kluasnuncoo', 'Adock Jid', 'Fagnom Maaluvreg', 'Trixiznueg Sud', 'Gaveterlug Teeplum',
			 #elf males
			 'Koss Kadnenin', 'Vul Grah', 'Sian Helugih', 'Halvran Thonnon', 'Zumvan Yulvimvu', 'Thiga Tah', 'Elies Theyissin', 'Domunan Feh', 'Coriogres Seigohhih', 'Neironthalmas Komrol',
			 #elf females
			 'Meclo Monnares', 'Phogo Zhun', 'Pharvas Wilvrutha', 'Inthe Shaniol', 'Mucullas Munsamri', 'Tulyalmaess Con', 'Thovumea Zioyelsum', 'Tovaha Thuh', 'Siagiaroma Jelliuh', 'Fohanici Fallis',
			 #dwarf males
			 'Brels Ironpelt', 'Trag Mavuls', 'Or Fistbrand', 'Rold Jes', 'Boc Firebash', 'Srunfurd Kazmog', 'Strokod Wildblaze', 'Evols Grakkall', 'Feklug Stormshade', 'Daindryk Ghuck',
			 #dwarf females
			 'Khum Moltenpunch', 'Ye Byklud', 'So Deeppunch', 'Tim Beth', 'Ra Coldgem', 'Ghulgwas Ghamryd', 'Kivull Stoneflow', 'Ongu Bryngodd', 'Nuddal Embersurge', 'Gevlir Srob'
			]
	if inname == "rand":
		#Needs to be changed to pick correct racial/gender names
		if ingender == 'female':
			name = random.choice(names)
		elif ingender == 'male':
			name = random.choice(names)
		else:
			name = random.choice(names)
	else:
		#Currently only supports Core Races
		name = inname
	return (name, gender)