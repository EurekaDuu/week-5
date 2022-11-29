# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import os.path as path
import pandas as pd
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

def load_input(player, p1Name, p2Name):
    if player == "X":
        playerName = p1Name
    else:
        playerName = p2Name
    x = input("Player " + playerName + "(" +player + ")" + ": Please input your move on x-coordinate (0 or 1 or 2):")
    while is_input_valid(x) != True:
        x = input("Player " + playerName + "(" +player + ")" + ": Please input your move on x-coordinate (0 or 1 or 2):")
    y = input("Player " + playerName + "(" +player + ")" + ": Please input your move on y-coordinate (0 or 1 or 2):")
    while is_input_valid(y) != True:
        y = input("Player " + playerName + "(" +player + ")" + ": Please input your move on y-coordinate (0 or 1 or 2):")

    return x, y

if __name__ == '__main__':
    game = logic.Game()
    winner = None
    player = logic.Player("X")


    isSinglePlayer = input("Single player please enter 1, Two players please enter 2:")
    while isSinglePlayer != "1" and isSinglePlayer != "2":
        isSinglePlayer = input("Single player please enter 1, Two players please enter 2:")

    if isSinglePlayer == "1":
        player1 = input("Please enter player name:")
        player2 = ""
    else:
        player1 = input("Please enter player1 name:")
        player2 = input("Please enter player2 name:")
    #
    while winner == None:
        # TODO: Show the board to the user.
        show_board(game.board)
        # TODO: Input a move from the player.
        if isSinglePlayer == "2" or player.name == "X":
            player.x_move, player.y_move = load_input(player.name, player1, player2)
            while is_coordinate_valid(game.board, int(player.x_move), int(player.y_move)) != True:
                print("Please input a coordinate that not been taken!")
                player.x_move, player.y_move = load_input(player.name, player1, player2)
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
                player1Status = -1
            else:
                if winner == "X":
                    print("Player " + player1 + " wins!!")
                    player1Status = 1
                    player2Status = -1
                else:
                    print("Player " + player2 + " wins!!")
                    player1Status = -1
                    player2Status = 1

            show_board(game.board)
        elif winner == "Draw":
            print("Draw! Game ends!")
            player1Status = 0
            player2Status = 0
            show_board(game.board)
        else:
            player = logic.Player(game.other_player(player.name))

    if player1Status == 1:
        player_data = pd.DataFrame([[player1, 1, 0, 0, 2]], columns=['player', 'wins', 'losses', 'draws', 'total_score'])
    if player1Status == 0:
        player_data = pd.DataFrame([[player1, 0, 0, 1, 1]], columns=['player', 'wins', 'losses', 'draws', 'total_score'])
    if player1Status == -1:
        player_data = pd.DataFrame([[player1, 0, 1, 0, 0]], columns=['player', 'wins', 'losses', 'draws', 'total_score'])

    if isSinglePlayer == "2":
        if player2Status == 1:
            player2_data = pd.DataFrame([[player2, 1, 0, 0, 2]], columns=['player', 'wins', 'losses', 'draws', 'total_score'])
        if player2Status == 0:
            player2_data = pd.DataFrame([[player2, 0, 0, 1, 1]], columns=['player', 'wins', 'losses', 'draws', 'total_score'])
        if player2Status == -1:
            player2_data = pd.DataFrame([[player2, 0, 1, 0, 0]], columns=['player', 'wins', 'losses', 'draws', 'total_score'])
        player_data = pd.concat([player_data, player2_data])

    if path.exists('tictactoe_global_data.csv') != False:
        load_player_data = pd.read_csv('tictactoe_global_data.csv')
        player_data = pd.concat([player_data, load_player_data])

        aggregation_functions = {'wins': 'sum', 'losses': 'sum', 'draws': 'sum', 'total_score': 'sum'}
        player_data = player_data.groupby(player_data['player'], sort = True).aggregate(aggregation_functions).reset_index()

    player_data = player_data.sort_values(by=['total_score'], ascending=False).reset_index(drop=True)

    print("Players performance:")
    if isSinglePlayer == "2":
        options=[player1, player2]
        print(player_data.loc[player_data['player'].isin(options)])
        player1_rank = player_data.loc[player_data['player'] == player1].index.tolist()[0] + 1
        player2_rank = player_data.loc[player_data['player'] == player2].index.tolist()[0] + 1
        print("player " + player1 + " global rank is: " + str(player1_rank))
        print("player " + player2 + " global rank is: " + str(player2_rank))
    else:
        print(player_data.loc[player_data['player'] == player1])
        player1_rank = player_data.loc[player_data['player'] == player1].index.tolist()[0] + 1
        print("player " + player1 + " global rank is: " + str(player1_rank))

    player_data.to_csv('tictactoe_global_data.csv')
