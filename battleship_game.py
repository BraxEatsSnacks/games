# *******************
# BraxEatsSnacks
# Battleship Game
# *******************

import battleship as bs


def main():
    """Executes battleship game function"""
    # play again loop
    again = "y"
    while again == "yes" or again == "y":
        play_game()
        again = input("Would you like to play again? ")
        print()
    print("So long sucker!")


def play_game():
    """Plays Battleship"""
    #generate menu
    bs.display_menu()

    #difficulty levels consisting of difficulty variables
    choice = 0
    game = 0
    while choice != 5 and game != 1:
        choice = int(input("\nWhat difficulty level? "))
        if choice == 1:
            variable = 3
            print("Okay! Starting the game... \n")
        elif choice == 2:
            variable = 5
            print("Okay! Starting the game... \n")
        elif choice == 3:
            variable = 7
            print("Okay! Starting the game... \n")
        elif choice == 4:
            variable = 9
            print("Okay, but its your funeral! Starting the game... \n")
        elif choice == 5:
            print("Exiting this game...")
            break
        else:
            print("That wasn't a valid input. \n")

        print("Turn 1 \n")
        turn = 1
        #generate board according to difficulty
        board = bs.generate_board(variable)
        #print board
        bs.print_board(board)
        print()

        #generate ship location
        ship_row = bs.random_row(board)
        ship_column = bs.random_column(board)
        """troubleshoot
        print(ship_row)
        print(ship_column)"""

        #guessing
        game = 0

        while game == 0:
            guess_row = int(input("Guess row: ")) - 1 #account for index 0
            guess_column = int(input("Guess column: ")) - 1 #ditto

            #win
            if guess_row == ship_row and guess_column == ship_column:
                print("Congratulations! You sunk my battleship!\n")
                game = 1
            #not win
            else:
                #out of range
                if (guess_row < 0 or guess_column < 0) or \
                    (guess_row > (variable - 1) or \
                        guess_column > (variable - 1)):
                    print("Oops, that's not even in the ocean. \n")
                    #guess previous guess
                elif board[guess_row][guess_column] == "X":
                    print("You guessed that one already. \n")
                #miss
                else:
                    print("You missed my battleship! \n")
                    board[guess_row][guess_column] = "X"
                #turncounter
                turn += 1
                print("Turn",turn,"\n")
                #updated board
                bs.print_board(board)
                print()

#call main function
# main()
