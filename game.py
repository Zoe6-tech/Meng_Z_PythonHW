#import the random package so that we can generate a random choice 
from random import randint
from gameFunctions import winlose
#set the computer variable to one of these choices(0,1,2)
player_lives = 1
computer_lives =1
#choices is an array => an array is a container that can hold multiple values 
#0, 1, 2
choices = ["rock","paper","scissors"]
#set the computer variable to one of these choices
computer = choices[randint(0,2)]
#set up the game loop so that we dont have to restart all the time
player = False
#define a python function that takes an argument



while player is False: 
	#set player to ture
	print("**********************************************\n\n")
	print("Computer Lives:", computer_lives,"/5\n")
	print("Player Lives:", player_lives,"/5\n")
	print("Choose your weapon!\n\n")
	print("**********************************************\n\n")
   
	player = input("choose rock, paper or scissors\n")
	player = player.lower()

	print("computer chose:", computer, "\n")
	print("player chose: ", player, "\n")

	if player.lower() == "quit":
		exit()

	elif computer == player:
		print("Tie! No one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("Your lose!",computer,"covers",player,"\n")
			player_lives = player_lives - 1
		else:
			print("Your win!",player,"smashes",computer,"\n")
			computer_lives = computer_lives - 1
 
	elif player.lower() == "paper":
		if computer == "scissors":
			print("Your lose!",computer,"cuts",player,"\n")
			player_lives = player_lives - 1
		else:
			print("Your win!",player,"covers",computer,"\n")
			computer_lives = computer_lives - 1

	elif player.lower() == "scissors":
		if computer == "rock":
			print("Your lose!",computer,"smashes",player,"\n")
			player_lives = player_lives - 1
		else:
			print("Your win!",player,"cuts",computer,"\n")
			computer_lives = computer_lives - 1
	else:
		print("That is not available input,please try again: choose rock, paper or scissors")

	# handle what happen when one of player got zero
	if player_lives is 0:
		winlose.winorlose("lost")
		#print("Out of lives! You suck at this game. Would you like to play again? Y or N")
		#choice = input("Y/N")
		#print(choice)
		#if (choice is "n") or (choice is "N"):
		#	print("You choice is quit")
		#	exit()
		#elif(choice is "y") or (choice is "Y"):
			#reset the game to that we can start all over again
		#	player_lives = 5
		#	computer_lives = 5
		#	player = False
		#	computer = choice[randint(0,2)]

	elif computer_lives is 0:
		winlose.winorlose("won")
		#print("Computer is out lives! You rock at this game. Would you like to play again? Y or N")
		#choice = input("Y/N")
		#print(choice)
		#if (choice is "n") or (choice is "N"):
		#	print("Computer choice is quit")
		#	exit()

		#elif(choice is "y") or (choice is "Y"):
			#reset the game to that we can start all over again
		#	player_lives = 5
		#	computer_lives = 5
		#	player = False
		#	computer = choice[randint(0,2)]
	else:
		#need to check all of our condition after checking for a tie
		player = False
		computer = choices[randint(0,2)]

	
