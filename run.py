from random import randint


COMP_BOARD = [[" "] * 5 for x in range(5)]
PLAYER_BOARD = [[" "] * 5 for x in range(5)]
GUESS_BOARD = [[" "] * 5 for x in range(5)]
COMP_GUESS_BOARD = [[" "] * 5 for x in range(5)]


letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}


def print_board(board):
    """
    Creates game boards.
    """
    print("  A B C D E")
    print("  ---------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def make_ships(board):
    """
    Populates the boards with ships.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = player_input()
        board[ship_row][ship_column] = "X"


def player_input():
    """
    Requests and validates input from player.
    """
    row = input("Please input ship row 1-5: ")
    while row not in "12345":
        print("Please input valid row!")
        row = input("Please input ship row 1-5: ")
    column = input("Please input ship column A-E: ").upper()
    while column not in "ABCDE":
        print("Please input valid column!")
        column = input("Please input ship column A-E: ").upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hits(board):
    """
    Counts how many ships have been sunk.
    """
    count = 0
    for row in board:
        for column in row:
            if column == "*":
                count += 1
    return count


def computer_input(PLAYER_BOARD):
    """
    Generates the computers choice and prints it to the players board.
    """
    row, column = randint(0, 4), randint(0, 4)
    if PLAYER_BOARD[row][column] == "-":
        computer_input(PLAYER_BOARD)
    elif PLAYER_BOARD[row][column] == " ":
        PLAYER_BOARD[row][column] = "-"
        print("Computer MISSED!")
    elif PLAYER_BOARD[row][column] == "X":
        PLAYER_BOARD[row][column] = "*"
        print("Computer HIT!")
    else:
        print("Computer MISS!")


def play_game():
    """
    Main game function, prints instructions, tallys turns, checks for
    repeat guesses, calls other functions and gives user result.
    """
    turns = 8
    while turns > 0:
        print("Welcome to BATTLESHIPS!")
        print("Players Board")
        print_board(PLAYER_BOARD)
        print("Computers Board")
        print_board(GUESS_BOARD)
        row, column = player_input()
        if GUESS_BOARD[row][column] == "-":
            print("Already guessed that!")
        elif COMP_BOARD[row][column] == "X":
            print("HIT!")
            GUESS_BOARD[row][column] = "*"
            turns -= 1
            computer_input(PLAYER_BOARD)
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
            computer_input(PLAYER_BOARD)
        if count_hits(GUESS_BOARD) == 5:
            print("Congrats, YOU WIN!")
            break
        print("You have " + str(turns) + " turns remaining")
        if turns == 0:
            print("GAME OVER!")
            break


make_ships(COMP_BOARD)
make_ships(PLAYER_BOARD)
play_game()
