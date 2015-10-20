import battleship_game as battle
import bc_game as bulls_cows
import hangman_game as hang
import os


def main():
	response = "y"
	count = 0
	while response != "no" or response != "n":
		# round 1
		if count < 1:
			response = input("Hey buddy. Wanna play a game? ").lower()
		# round > 1
		else:
			response = input("Hey buddy. Wanna play ANOTHER game? ").lower()
		#play game
		if response == "yes" or response == "y":
			print("Excellent... Live or die. Make your choice...\nJust kidding!\n")
			menu_choices()
			game_choice()
			print()

			count += 1
		else:
			print("Alright chump! Maybe next time!")
			break

def game_choice():
	"""game selection"""
	options = [1,2,3,4]
	option = int(input("What game are we gonna play, homie? "))

	# battelship
	if option == 1:
		battle.main()
	# bulls & cows
	elif option == 2:
		bulls_cows.main()
	# hangman
	elif option == 3:
		hang.main()
	# rock paper scissors (java)
	elif option == 4:
		os.system("javac rock_paper_scissors.java && javac rps_game.java")
		os.system("java rps_game")

def menu_choices():
	"""menu of choices"""
	print("*************************")
	print("1) Battleship")
	print("2) Bulls & Cows")
	print("3) Hangman")
	print("4) Rock Paper Scissors")
	print("*************************")
	print()

main()