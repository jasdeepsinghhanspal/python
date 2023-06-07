//tic tac toe game in python
import tkinter as tk
from tkinter import messagebox

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
BOARD_SIZE = 3

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Variables
current_player = PLAYER_X
board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
buttons = []

# Function to handle button click
def on_button_click(row, col):
    global current_player

    if board[row][col] == EMPTY:
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player

        # Check for a win
        if check_win(current_player):
            messagebox.showinfo("Game Over", "Player {} wins!".format(current_player))
            reset_game()
        # Check for a draw
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

# Function to check for a win
def check_win(player):
    for i in range(BOARD_SIZE):
        # Check rows
        if all(cell == player for cell in board[i]):
            return True
        # Check columns
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Function to check for a draw
def check_draw():
    for row in board:
        if any(cell == EMPTY for cell in row):
            return False
    return True

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = PLAYER_X
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            buttons[row][col].config(text=EMPTY)

# Create and place buttons
for row in range(BOARD_SIZE):
    button_row = []
    for col in range(BOARD_SIZE):
        button = tk.Button(window, text=EMPTY, font=("Arial", 24), width=4, height=2,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Start the main loop
window.mainloop()

