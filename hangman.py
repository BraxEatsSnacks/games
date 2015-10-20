# ********************************
# Hangman Test Code
# BraxEatsSnacks & BusterBladeZX
# ********************************

import random

# ****************************************************************************#

def generate_menu():
    """Creates menu of options for game"""
    print()
    print("Welcome to Hangman!")
    print("Please select a difficulty below:\n")
    print("* Easy\n* Medium\n* Hard\n")

# ****************************************************************************#

def difficulty_choice(word_banks):
    """Allows user choice of difficulty returning category of word & word as key: value pair respectively"""
    choice = 0
    while (choice != "easy") and (choice != "medium") and (choice != "hard"):
        choice = input().lower()
        print()
        if choice == "easy":
            lvl = 0
        elif choice == "medium":
            lvl = 1
        elif choice == "hard":
            lvl = 2
        else:
            print("Sorry what did you mean? ")

    # choice of word category
    random_num = random.randint(0, 1)

    if random_num == 0:
        category = "food"
    elif random_num == 1:
        category = "sports"

    # choice of word itself
    index = random.randint(0, len(word_banks[lvl][category])-1)
    word = word_banks[lvl][category][index]

    return {category: word}

# ****************************************************************************#

def draw_noose(limbs):
    """Draws updateable noose pseudo-image"""
    line1 = "  ________"
    line2 = "  |/\t|"
    line3 = "  |"
    head = "  |\tO"
    line4 = "  |"
    body = "  |\t|"
    l_arm = "  |    /|"
    r_arm = "  |    /|\\"
    line5 = " /|\\"
    l_leg = " /|\\\t/"
    r_leg = " /|\\ \t/\\"
    line6 = "/ | \\"

    if limbs == 0:
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)
        print(line6)
        print()
    elif limbs == 1:
        print(line1)
        print(line2)
        print(head)
        print(line4)
        print(line5)
        print(line6)
        print()
    elif limbs == 2:
        print(line1)
        print(line2)
        print(head)
        print(body)
        print(line5)
        print(line6)
        print()
    elif limbs == 3:
        print(line1)
        print(line2)
        print(head)
        print(l_arm)
        print(line5)
        print(line6)
        print()
    elif limbs == 4:
        print(line1)
        print(line2)
        print(head)
        print(r_arm)
        print(line5)
        print(line6)
        print()
    elif limbs == 5:
        print(line1)
        print(line2)
        print(head)
        print(r_arm)
        print(l_leg)
        print(line6)
        print()
    elif limbs == 6:
        print(line1)
        print(line2)
        print(head)
        print(r_arm)
        print(r_leg)
        print(line6)
        print()

# ****************************************************************************#

def game_loop(word, category):
    """Primary game loop"""
    # game letters in list
    correct = list(word)

    # empty list to which append incorrect guessed letters
    incorrect = []

    # draw empty noose
    limbs = 0
    draw_noose(limbs)

    # print blanks
    answer = [("_") for letter in correct]
    print(" ".join(answer))

    # loop
    hanged = False
    hinted = 0
    while hanged == False:
        # user guess letter
        guess = input("What letter would you like to guess? ").lower()
        print()

        while len(guess) > 1:
            guess = input("Please only 1 letter. Try again: ")
            
        # Match answer with guess
        correct_letter = 0
        for i in range(0, len(correct)):
            if guess == correct[i]:
                correct_letter += 1
                answer[i] = guess
        # wrong guess adds limbs & letter to displayed list
        if correct_letter == 0 and guess not in incorrect:
            incorrect.append(guess)
            limbs += 1

        # update wrong letter list
        if len(incorrect) >= 1:
            print("Wrong Letters: ", str(incorrect))
            
        # update noose
        draw_noose(limbs)
        
        # update blanks with letter placements
        print(" ".join(answer))

        # Hint
        if (limbs >= 3) and (hinted == 0):
            hinted = hint(category)

        # Lose
        if limbs == 6:
            print("Sorry, you lose! The word was %s! Better luck next time!" % (word.upper()))
            hanged = True

        # Win
        if answer == correct:
            print("Congratulations, you won!")
            hanged = True

# ****************************************************************************#

def hint(category):
    """Offers a hint if user struggles"""
    hint_or_nah = input("Would you like a hint? ").lower()
    # YES
    if hint_or_nah == "yes" or hint_or_nah == "y":
        print("The category is %s.\n" % (category))
        already = 1
    # NO
    else:
        print("Alrighty then! Good luck.")
        already = 0

    return already
