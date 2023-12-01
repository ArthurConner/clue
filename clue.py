import clue.gameplay as clue

p1 = ("user",True,clue.getPlay)
s1 = ("simple",False,clue.mimic(4,clue.rWalk))
hr1 = ("half",False,clue.halfRight(clue.rWalk))
strategies = [hr1,hr1,p1,s1,s1]
clue.runVisualGame(strategies)