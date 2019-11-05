from random import randint
#define a python function that takes an argument
def winorlose(status):
	#stsues will ne wither won or lost - you passing this in as am agrument
	print("called win or lose")
	print("*****************************")

	print("You",status, "! Would you like to play again?")
	choice = input("Y / N")
	print(choice)

	if (choice is "n") or (choice is "N"):
		print("You choice is quit")
		exit()

	elif(choice is "y") or (choice is "Y"):
	#reset the game to that we can start alls over again
		global player_lives
		global computer_lives
		global player
		global computer
		global choices

		player_lives = 1
		computer_lives = 1
		player = False
		computer = choices[randint(0,2)]