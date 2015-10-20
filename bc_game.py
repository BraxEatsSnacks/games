#*********************
# Braxton Gunter
# Bulls and Cows Game
#*********************

import bulls_and_cows as bc

#execute Bulls and Cows
def main():
    print("Welcome to Bulls and Cows death match!")
    again = "y"
    while again == "y":
          play_game()
          again = input("Would you like to play again? (y/n) ")
    print("So long sucker!")


def play_game():
    """Plays one interactive game of bulls and cows on the console"""
    print("Remember Cows are correct digits in the wrong place while Bulls are correct digits in the correct place!")
    print()
    print("The 4 digit secret number is generated.")
    #generate secret number
    answer = bc.generate_secret()
    bulls = 0
    turnCounter = 1 #round
    #print(answer)

    #meat and potatoes
    while bulls != 4:
        print("Round: " + str(turnCounter) + "\n")
        #ask user for number guess
        guess = input("Alright, what is your guess? (Remember no repeating digits!) ")
        while len(guess) != 4:
            print("The guess has to be 4 digits long!")
            guess = input("Alright, what is your guess? (Remember no repeating digits!) ")

        #import counting functions
        bulls = bc.count_bulls(guess, answer)
        cows = bc.count_cows(guess, answer)

        print("Bulls: " + str(bulls))
        print("Cows: " + str(cows))
        turnCounter = turnCounter + 1

    if bulls == 4 and turnCounter <= 15:
        print("Congratulations! You won, and rather quickly at that!")

    elif bulls == 4 and turnCounter > 15:
        print("Congratulations...I guess...you won, but it took you long.")
        print("Whatever.")

#call the main function
# main()