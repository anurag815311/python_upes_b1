import tkinter as tk
from tkinter import messagebox

# Function to start a new game
def new_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for button in row:
            button.config(text="", state="normal", bg="white")
    label.config(text="Player X's turn")

# Function to check for winner
def check_winner():
    for i in range(3):
        # Check rows
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            return buttons[i][0]['text']
        # Check columns
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            return buttons[0][i]['text']
    
    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return buttons[0][2]['text']

    # Check for draw
    for row in buttons:
        for button in row:
            if button['text'] == "":
                return None  # The game is not over yet

    return "Draw"

# Function to handle button click
def button_click(row, col):
    global current_player

    # If the button is already clicked, do nothing
    if buttons[row][col]['text'] != "":
        return

    # Set the button text to the current player's symbol
    buttons[row][col].config(text=current_player, state="disabled")

    # Check if there's a winner or draw
    winner = check_winner()

    if winner == "X":
        messagebox.showinfo("Game Over", "Player X wins!")
        new_game()
    elif winner == "O":
        messagebox.showinfo("Game Over", "Player O wins!")
        new_game()
    elif winner == "Draw":
        messagebox.showinfo("Game Over", "It's a draw!")
        new_game()
    else:
        # Switch to the next player
        current_player = "O" if current_player == "X" else "X"
        label.config(text=f"Player {current_player}'s turn")

# Initialize the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Player 'X' starts first
current_player = "X"

# Create a label to display whose turn it is
label = tk.Label(root, text="Player X's turn", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=10)

# Create a 3x3 grid of buttons
buttons = [[None, None, None] for _ in range(3)]  # Initialize a 3x3 array for buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, font=("Helvetica", 24), 
                                  command=lambda row=i, col=j: button_click(row, col), bg="white")
        buttons[i][j].grid(row=i+1, column=j)  # Add buttons to the grid, with offset to leave row 0 for label

# Create a "New Game" button
new_game_button = tk.Button(root, text="New Game", command=new_game, font=("Helvetica", 12), width=20)
new_game_button.grid(row=4, column=0, columnspan=3, pady=10)

# Start the first game
new_game()

# Run the Tkinter event loop
root.mainloop()


