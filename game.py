#import the random package so that we can generate a random choice 
from random import randint

#choices is an array => an array is a container that can hold multiple values 
#0, 1, 2
choices = ["rock","paper","scissors"]

#set the computer variable to one of these choices
computer = choices[randint(0,2)]

#set up the game loop so that we dont have to restart all the time
player = False

while player is False: 
	#set player to ture
	player = input("choose rock, paper and scissors\n")

	print("computer chose:", computer, "\n")
	print("player chose: ", player, "\n")

	if player == "quit":
		exit()
	elif computer == player:
		print("Tie! No one wins, play again")
	#need to check all of our condition after checking for a tie
	player = False
	computer = choices[randint(0,2)]
