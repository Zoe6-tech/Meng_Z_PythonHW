from random import randint
def comparison(choices): 
	# status will be either won or lost - you're passing this in as an argument
	print(choices)
	print("************************")
player_lives = 1
computer_lives = 1
player = False
choices = ["rock","paper","scissors"]
computer = choices[randint(0,2)]

if player == "quit":
		exit()
elif computer == player:
		print("tie! no one wins, play again")

elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1

elif player == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "covers", computer, "\n")
			computer_lives = computer_lives - 1

elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1

else:
		print("That's not a valid choice, try again")