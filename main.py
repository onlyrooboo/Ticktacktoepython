import json
import random

board = [[0 for _ in range(3)] for _ in range(3)]
player_turn = True

def bot_move(current_board):
    # Bot naturally finds (row, col)
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if current_board[row][col] != 0: # If the cell is occupied, find another
        return bot_move(current_board)
    return row, col

def row_col_processer():
    imput = int(input(f"Player 1 (Human), enter (1-9): "))
    row = (imput - 1) // 3
    col = (imput - 1) % 3
    if board[row][col] != 0: # If the cell is occupied, ask for input again
        print("Cell already occupied! Try again.")
        return row_col_processer()
    return row, col # Changed from col, row to match standard

def board_update(row, col):
    # standard indexing: board[row][col]
    board[row][col] = 1 if player_turn else 2

def turn_switcher():
    global player_turn
    player_turn = not player_turn

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    
    return None



# Main Game Loop
while True:
    for row_list in board:
        print([ '-' if cell == 0 else "X" if cell == 1 else "O" for cell in row_list ]) # Print the board with 0 as "."

    if player_turn: 
        r, c = row_col_processer()
    else:            
        print("Bot is thinking...")
        r, c = bot_move(board) # Pass the board in!
    
    board_update(r, c)
    turn_switcher()
    print("-" * 10)

    winner = check_winner()
    if winner:
        print(f"Player {winner} wins!")
        print("Final Board:")
        for row_list in board:
            print([ '-' if cell == 0 else "X" if cell == 1 else "O" for cell in row_list ])
        break