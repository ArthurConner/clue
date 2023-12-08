import clue.gameplay as clue

p1 = ("user",True,clue.getPlay)
s1 = ("simple",False,clue.mimic(4,clue.rWalk))
hr1 = ("half",False,clue.halfRight(clue.rWalk))
s2 = ("simple r",False,clue.repeater([clue.mimic(-1,clue.rWalk) for x in range(4)]))
b2 = ("better rZ",False,clue.repeater([clue.mimic(8,clue.rWalk) for x in range(4)]))

strategies = [b2,hr1,p1,s1,s2]
clue.runVisualGame(strategies)
