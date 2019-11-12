# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose
from gameFunctions import gameVars
from gameFunctions import compare

while gameVars.player is False:
	# set player to True
	print("======================================================================")
	print("Round",gameVars.Round+1,"\n")
	print("Computer lives: ",gameVars.computer_lives, "/",gameVars.total_lives,"\n")
	print("Player lives: ",gameVars.player_lives, "/",gameVars.total_lives,"\n")
	print("**********************************")
	print("Choose your weapon first!")
	

	gameVars.player = input("Choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()
	
	print("\n**********************************")
	print("computer chose: ", gameVars.computer, "\n")
	print("player chose: ", gameVars.player, "\n")
	print("**********************************")

	#this is where you call compare
	
	if gameVars.player.lower() == "quit":
		compare.comparechoices("quit")
	elif gameVars.player.lower() == "rock":
		compare.comparechoices("rock")
	elif gameVars.player.lower() == "paper":
		compare.comparechoices("paper")
	elif gameVars.player.lower() == "scissors":
		compare.comparechoices("scissors")
	else:
		print("That's not a valid choice, please try again!")
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0,2)]

	# if gameVars.player.lower() == "quit":
	# 	print("Your chose " + status, ". Game Over!")
	# 	exit()
	# elif gameVars.computer_lives == gameVars.player:
	# 	print("tie! no one wins, play again")
	# 	gameVars.Round=gameVars.Round+1

	# elif gameVars.player.lower() == "rock":
	# 	if gameVars.computer == "paper":
	# 		print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives - 1
	# 		gameVars.Round=gameVars.Round+1
	# 	else:
	# 		print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1
	# 		gameVars.Round=gameVars.Round+1

	# elif gameVars.player.lower() == "paper":
	# 	if gameVars.computer == "scissors":
	# 		print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives - 1
	# 		gameVars.Round=gameVars.Round+1
	# 	else:
	# 		print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1
	# 		gameVars.Round=gameVars.Round+1

	# elif gameVars.player.lower() == "scissors":
	# 	if gameVars.computer == "rock":
	# 		print("Your lose!",gameVars.computer,"smashes",gameVars.player,"\n")
	# 		gameVars.player_lives = gameVars.player_lives - 1
	# 		gameVars.Round=gameVars.Round+1
	# 	else:
	# 		print("Your win!",gameVars.player,"cuts",gameVars.computer,"\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1
	# 		gameVars.Round=gameVars.Round+1

	# else:
	# 	print("That's not a valid choice, try again")


	# handle all lives lost for player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")
		# print("Out of lives! You suck at this game. Would you like to play again?\n")
		# choice = input("Y / N")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	# reset the game so that we can start all over again
		# 	player_lives = 5
		# 	gameVars.computer_lives_lives = 5
		# 	player = False
		# 	gameVars.computer_lives = choices[randint(0,2)]


	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
		# print("gameVars.computer_lives is out of lives! You rock at this game. Would you like to play again?\n")
		# choice = input("Y / N")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	# reset the game so that we can start all over again
		# 	player_lives = 5
		# 	gameVars.computer_lives_lives = 5
		# 	player = False
		# 	gameVars.computer_lives = choices[randint(0,2)]

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.computer = gameVars.choices[randint(0, 2)]