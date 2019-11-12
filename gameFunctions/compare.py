from random import randint
from gameFunctions import gameVars
#what you are trying to compare the function?
#you will need to pass those things in as agruments
#inside the round brackets
def comparechoices():

	if gameVars.player.lower() == "quit":
		exit()
	elif gameVars.computer_lives == gameVars.player:
		print("tie! no one wins, play again")

	elif gameVars.player.lower() == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player.lower() == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")