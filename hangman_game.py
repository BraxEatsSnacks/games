# ********************************
# Hangman Game
# BraxEatsSnacks & BusterBladeZX
# ********************************

from hangman import *

# SEE "hangman.py" FOR TROUBLESHOOTING

# ******************************* word banks ********************************* #

easy = {"food": ["apple", "banana", "chicken", "orange"], "sports": ["football", "soccer", "rugby", "basketball", "polo", "swim"]}
medium = {"food": ["caviar", "macaroon","wasabi", "guacomole", "hazelnut", "walnut", "coconut", "cauliflower", "carbohydrate", "alfalfa"], "sports": ["pentathlon", "windsurfing", "aerobics", "gymnasium", "skateboarding", "unicycle"]}
hard = {"food": ["sauerkraut", "zucchini", "licorice", "calimari"], "sports": ["parasailing", "olympics", "zorbing", "parkour", "snorkelling", "quidditch"]}

word_banks = [easy , medium, hard]

# **************************************************************************** #

def main():
    """Main Execution"""
    again = "yes"
    while (again == "yes") or (again == "y"):

        game()
    
        again = input("Would you like to play again? ")
        print()
    else:
        print("So long sucker!")
        
def game():
    """Hangman Game Function"""
    # display menu
    generate_menu()

    # user can choose difficulty
    pair = difficulty_choice(word_banks)

    # unpack variables from dictionary
    category = [key for key in pair]
    category = str(category[0])
    word = pair[category]

    game_loop(word, category)

# call main function
# main()
