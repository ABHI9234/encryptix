import random

# Define the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a winner
def winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Best move function for AI
def best_move():
    best_score = float('-inf')
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Player move
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] == ' ':
            board[player_move] = 'X'
            if winner(board, 'X'):
                print_board()
                print("You win!")
                break
            elif is_board_full(board):
                print_board()
                print("It's a tie!")
                break

            # AI move
            ai_move = best_move()
            board[ai_move] = 'O'
            if winner(board, 'O'):
                print_board()
                print("You lose!")
                break
            elif is_board_full(board):
                print_board()
                print("It's a tie!")
                break
        else:
            print("Invalid move! Try again.")

        print_board()

play_game()
