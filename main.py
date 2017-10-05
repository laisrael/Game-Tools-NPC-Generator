import racegen, namegen, statgen, classgen, featgen
#Add item generation later

#Consolidate results and determine the final character
def main(inlevel, inrace='rand', inname='rand', instats='rand', inclass='rand', infeats='rand',):
	myrace = racegen.generate(inrace)
	myname = namegen.generate(inname, myrace.lower())
	mystats = statgen.generate(instats, inlevel)
	myclass = classgen.generate(inclass)
	myfeats = featgen.generate(inrace, inclass, infeats, inlevel)
	print("Your race is: " + myrace)
	print("Your name is: " + myname)
	print("Your stats are: " + mystats)
	print("Your class is: " + myclass)
	print("Your feats are: ")
	for i in myfeats:
		print(i)

main(10)