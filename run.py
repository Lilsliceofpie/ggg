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
            ship_row, ship_column = find_ship_location()
        board[ship_row][ship_column] = "X"


def find_ship_location():


def count_hits(board):


def comp_turn    