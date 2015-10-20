#*******************
# BraxEatsSnacks
# Battleship Code
#*******************

import random


def display_menu():
    """Generates menu that displays difficulty choices"""
    print()
    print("         Welcome to Battleship! ")
    print("* " * 20)
    print("* " + str(1) + " Easy")
    print("* " + str(2) + " Medium")
    print("* " + str(3) + " Hard")
    print("* " + str(4) + " You're Insane")
    print("* " + str(5) + " Quit")
    print("* " * 20)

def generate_board(variable):
    """Creates board/grid: size contingent upon some variable"""
    board = []
    for x in range(variable):
        board.append(["O"] * variable)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_column(board):
    return random.randint(0, len(board[0]) - 1)