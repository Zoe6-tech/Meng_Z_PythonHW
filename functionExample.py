#how to pass arguments into a function
from random import randint
from gameFunctions import gameVars

def compareStuff(thing1,thing2)
	if thing1==thing2:
		print('they match!')
	else:
		print('they do not match')

#invoke a function by writing its name(calling it)
#and passing agruments

compareStuff('stuff','stuff')#thing1,thing2

compareStuff('stuff','other stuff')

compareStuff(1,2)

compareStuff(1,2)     