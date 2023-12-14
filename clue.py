import clue.gameplay as clue
import sys
 
# total arguments
n = len(sys.argv)

if n > 1:
	x = sys.argv[1]
	print(x)
	clue.quickGame(int(x))
else:
	clue.quickGame(4)
	

