import clue.gameplay as clue


strategies = [("user",True,clue.getPlay),("simple",False,clue.simpleGuess),("simple",False,clue.simpleGuess)]
clue.runVisualGame(4,strategies)