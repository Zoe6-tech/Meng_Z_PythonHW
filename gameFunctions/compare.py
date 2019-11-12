from random import randint
from gameFunctions import gameVars
#what you are trying to compare the function?
#you will need to pass those things in as agruments
#inside the round brackets
def comparechoices(status):

	if gameVars.player.lower() == "quit":
		print("Your chose " + status, ". Game Over!")
		exit()
		
	elif gameVars.computer_lives == gameVars.player:
		print("tie! no one wins, play again")
		gameVars.Round=gameVars.Round+1
		
	elif gameVars.player.lower() == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
			gameVars.Round=gameVars.Round+1
		else:
			print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
			gameVars.Round=gameVars.Round+1

	elif gameVars.player.lower() == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
			gameVars.Round=gameVars.Round+1
		else:
			print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
			gameVars.Round=gameVars.Round+1

	elif gameVars.player.lower() == "scissors":
		if gameVars.computer == "rock":
			print("Your lose!",gameVars.computer,"smashes",gameVars.player,"\n")
			gameVars.player_lives = gameVars.player_lives - 1
			gameVars.Round=gameVars.Round+1
		else:
			print("Your win!",gameVars.player,"cuts",gameVars.computer,"\n")
			gameVars.computer_lives = gameVars.computer_lives - 1
			gameVars.Round=gameVars.Round+1
	else:
		print("That's not a valid choice, please try again!")

	print("Round ",gameVars.Round,"Finish!","\n")
	gameVars.player = False
	gameVars.computer = gameVars.choices[randint(0,2)]


