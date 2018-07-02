import racegen, namegen, statgen, classgen, featgen

#Consolidate results and determine the final character
def main():
	inlevel = int(input("What level should your NPC be?"))
	inrace = input("What race should your NPC be? If you would like their race to be random, enter \"rand\"")
	inname = input("What is your NPC's name? If you would like their name to be random, enter \"rand\"")
	ingender = input("What is your NPC's gender? If you would like their gender to be random, enter \"rand\"")
	instats = input("What are your NPC's stats? Enter their stats as an array of the following format: [STR, DEX, CON, INT, WIS, CHA]\nIf you would like their stats to be random, enter \"rand\"")
	inclass = input("What is your NPC's class? If you would like their class to be random, enter \"rand\"")
	infeats = input("What are your NPC's feats? Enter their feats as an array of the following format: [Feat 1, Feat 2, ... , Feat n]\nIf you would like their feats to be random, enter \"rand\"")

	myrace, racestats = racegen.generate(inrace)
	myname, mygender = namegen.generate(inname, ingender, myrace.lower())
	myclass, statpref = classgen.generate(inclass)
	mystats = statgen.generate(instats, inlevel, racestats, statpref)
	myfeats = featgen.generate(myrace, myclass, mystats, infeats, inlevel)
	myskills = "Implementation Needed"
	print("Your race is: " + myrace)
	print("Your name is: " + myname)
	print("Your gender is: " + mygender.title())
	print("Your stats are: " + str(mystats))
	print("Your class is: " + myclass)
	print("Your feats are: ")
	for i in myfeats:
		print(i)
	print("Your skills are: " + myskills)

main()