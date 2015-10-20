# ****************************
# Braxton Gunter
# Bulls and Cows Programming
# ****************************

import random


def generate_secret():
    """Generates a 4 digit number with no repeat digits
    and converts the number to a string"""

    numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret = []

    while len(secret) < 4:
        # random index generation
        i = random.randint(0, len(numberList) - 1)

        #remove index and append to new list
        digit = numberList.pop(i - 1)
        secret.append(digit)

    # convert to conjoined string
    return "".join(map(str, secret))


def count_bulls(guess, answer):
    """Returns the number of bulls the guess
    earns when the secret number is answer"""

    bulls = 0

    #detect the amount of numbers that are same at same index
    for i in range(0, 4):
        if (guess[i] in answer) and (guess[i] == answer[i]):
            bulls = bulls + 1

    return bulls


def count_cows(guess, answer):
    """Returns the number of bulls the guess earns when the
    secret number is answer"""

    cows = 0
    bulls = count_bulls(guess,answer)

    #detect the amount of numbers that are same at different index
    for i in range(0, 4):
        if (guess[i] in answer) and (guess[i] != answer[i]):
            cows = cows + 1
        #cant count cows multiple times
        if (bulls >= 1) and (cows > 1):
            for i in guess:
                cows = cows - 1

    if cows < 0:
        cows = 0
    return cows


