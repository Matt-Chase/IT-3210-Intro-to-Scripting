"""
Matt Chase
Assignment 6
"""

def printgrades(sb, gb):

	sb.sort()
	gb.sort(reverse=True)

	print "\nScore  Grade"
	print "-----  -----"
	for s, g in zip(sb, gb):
		print "%-6s %s" % (s, g)
		
	print "\nThe lowest score is %s, %s" %(sb[0], gb[0])
	
	exit()


def getgrade(skor):
	if skor < 60:
		letter = "F"
	elif skor >= 60 and skor < 70:
		letter = "D"
	elif skor >= 70 and skor < 80:
		letter = "C"
	elif skor >= 80 and skor < 90:
		letter = "B"
	else:
		letter = "A"
	
	return letter
	
score = raw_input("Enter a score (\"end\" to stop) ")

scorebook = []
gradebook = []

while score != "end":
	intscore = int(score)

	grade = getgrade(intscore)
	
	scorebook.append(intscore)
	gradebook.append(grade)
	
	print(gradebook)
	
	score = raw_input("Enter a score (\"end\" to stop) ")

	
printgrades(scorebook, gradebook)
