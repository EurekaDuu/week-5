# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logic

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
    game = logic.Game()
    winner = None
    player = logic.Player("X")


    isSinglePlayer = input("Single player please enter 1, Two players please enter 2:")
    while isSinglePlayer != "1" and isSinglePlayer != "2":
        isSinglePlayer = input("Single player please enter 1, Two players please enter 2:")

    while winner == None:
        # TODO: Show the board to the user.
        show_board(game.board)
        # TODO: Input a move from the player.
        if isSinglePlayer == "2" or player.name == "X":
            player.x_move, player.y_move = load_input(player.name)
            while is_coordinate_valid(game.board, int(player.x_move), int(player.y_move)) != True:
                print("Please input a coordinate that not been taken!")
                player.x_move, player.y_move = load_input(player.name)
        else:
            player.x_move, player.y_move = game.get_bot_input()
            print("Bot took a move on [" + str(player.x_move) + ", " + str(player.y_move) + "]")
        # TODO: Update the board.
        game.update_board(int(player.x_move), int(player.y_move), player.name)
        # TODO: Update who's turn it is.
        winner = game.get_winner()
        if winner == "X" or winner == "O":
            if isSinglePlayer == "1" and winner == "O":
                print("Bot wins!!")
            else:
                print("Player " + player.name + " wins!!")
            show_board(game.board)
        elif winner == "Draw":
            print("Draw! Game ends!")
            show_board(game.board)
        else:
            player = logic.Player(game.other_player(player.name))
