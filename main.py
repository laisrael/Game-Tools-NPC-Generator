import racegen, namegen, statgen, classgen, featgen
#Add item generation later

#Consolidate results and determine the final character
def main(inlevel, inrace='rand', inname='rand', ingender='rand', instats='rand', inclass='rand', infeats='rand',):
	myrace = racegen.generate(inrace)
	myname, mygender = namegen.generate(inname, ingender, myrace.lower())
	myclass, statpref = classgen.generate(inclass)
	mystats = statgen.generate(instats, inlevel)
	myfeats = featgen.generate(inrace, inclass, infeats, inlevel)
	print("Your race is: " + myrace)
	print("Your name is: " + myname)
	print("Your gender is: " + mygender.title())
	print("Your stats are: " + mystats)
	print("Your class is: " + myclass)
	print("This is a test, your stat priority is; " + str(statpref))
	print("Your feats are: ")
	for i in myfeats:
		print(i)

main(10)