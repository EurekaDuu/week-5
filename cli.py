# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import other_player
from logic import update_board
from logic import get_winner
def show_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                print("_ ", end='')
            if board[i][j] == "X":
                print("X ", end='')
            if board[i][j] == "O":
                print("O ", end='')
        print("\n")

def is_input_valid(input):
    if input == "0" or input == "1" or input == "2":
        return True
    return False

def is_coordinate_valid(board, x, y):
    if board[x][y] is not None:
        return False
    return True

def load_input(player):
    x = input("Player "+player + ": Please input your move on x-coordinate (0 or 1 or 2):")
    while is_input_valid(x) != True:
        x = input("Player "+player + ": Please input your move on x-coordinate (0 or 1 or 2):")
    y = input("Player "+player + ": Please input your move on y-coordinate (0 or 1 or 2):")
    while is_input_valid(y) != True:
        y = input("Player "+player + ": Please input your move on y-coordinate (0 or 1 or 2):")

    return x, y

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = "X"
    while winner == None:
        # TODO: Show the board to the user.
        show_board(board)
        # TODO: Input a move from the player.
        x, y = load_input(player)
        while is_coordinate_valid(board, int(x), int(y)) != True:
            print("Please input a coordinate that not been taken!")
            x, y = load_input(player)
        # TODO: Update the board.
        update_board(board, int(x), int(y), player)
        # TODO: Update who's turn it is.
        winner = get_winner(board)
        if winner == "X" or winner == "O":
            print("Player "+player + " wins!!")
            show_board(board)
        elif winner == "Draw":
            print("Draw! Game ends!")
            show_board(board)
        else:
            player = other_player(player)

