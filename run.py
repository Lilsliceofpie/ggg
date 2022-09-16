from random import randint


HIDDEN_BOARD = [[" "] * 5 for x in range(5)]
PLAYER_BOARD = [[" "] * 5 for x in range(5)]
GUESS_BOARD = [[" "] * 5 for x in range(5)]
COMP_GUESS_BOARD = [[" "] * 5 for x in range(5)]


letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}


def print_board(board):
    print("  A B C D E")
    print("  ---------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def make_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = player_input()
        board[ship_row][ship_column] = "X"


def player_input():
    row = input("Please enter ship row 1-5:")
    while row not in "12345":
        print("Please enter valid row!")
        row = input("Please enter ship row 1-5:")
    column = input("Please enter ship column A-E:").upper()
    while column not in "ABCDE":
        print("Please enter valid column!")
        column = input("Please enter ship column A-E:").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hits(board):


def computer_input()