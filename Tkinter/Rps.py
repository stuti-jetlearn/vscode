# Import everything from tkinter for GUI
from tkinter import *

# Import font module to customize text fonts
import tkinter.font as font

# Import random module to let computer choose randomly
import random

# Initialize player and computer scores
player_score = 0
computer_score = 0

# Available options: (name, number)
# rock = 0, paper = 1, scissors = 2
options = [('rock', 0), ('paper', 1), ('scissors', 2)]


# Function called when computer wins
def computer_wins():
    global computer_score, player_score

    # Increase computer score by 1
    computer_score += 1

    # Display winner message
    winner_label.config(text="Computer Won!!!")

    # Update score labels
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))


# Function called when player wins
def player_wins():
    global computer_score, player_score

    # Increase player score by 1
    player_score += 1

    # Display winner message
    winner_label.config(text="Player Won!!!")

    # Update score labels
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))


# Function called when game is a tie
def tie():
    global computer_score, player_score

    # Display tie message
    winner_label.config(text="TIE!!!")

    # Update score labels (no score change)
    computer_score_label.config(text='Computer Score : ' + str(computer_score))
    player_score_label.config(text='Player Score : ' + str(player_score))


# Function that runs when player clicks a button
def player_choice(player_input):
    global player_score, computer_score

    # Print player's choice (for debugging)
    print(player_input)

    # Get random choice from computer
    computer_input = get_computer_choice()
    print(computer_input)

    # Update labels showing selections
    player_choice_label.config(text='Your Selected : ' + player_input[0])
    computer_choice_label.config(text='Computer Selected : ' + computer_input[0])

    # If both choose same option → tie
    if player_input == computer_input:
        tie()

    # If player chooses ROCK
    if player_input[1] == 0:
        if computer_input[1] == 1:
            computer_wins()   # paper beats rock
        elif computer_input[1] == 2:
            player_wins()    # rock beats scissors

    # If player chooses PAPER
    elif player_input[1] == 1:
        if computer_input[1] == 0:
            player_wins()    # paper beats rock
        elif computer_input[1] == 2:
            computer_wins()  # scissors beats paper

    # If player chooses SCISSORS
    elif player_input[1] == 2:
        if computer_input[1] == 0:
            computer_wins()  # rock beats scissors
        elif computer_input[1] == 1:
            player_wins()   # scissors beats paper


# Function to randomly select computer's choice
def get_computer_choice():
    return random.choice(options)


# Create main application window
game_window = Tk()

# Set window title
game_window.title("Rock Paper Scissors Game")

# Define common font style
app_font = font.Font(size=12)


# Game title label
game_title = Label(
    text='Rock Paper Scissors',
    font=font.Font(size=20),
    fg='grey'
)
game_title.pack()


# Label to display who won
winner_label = Label(
    text="Let's Start the Game...",
    fg='green',
    font=font.Font(size=13),
    pady=8
)
winner_label.pack()


# Frame to hold buttons and labels
input_frame = Frame(game_window)
input_frame.pack()


# Label for player options
player_options = Label(
    input_frame,
    text="Your Options : ",
    font=app_font,
    fg='grey'
)
player_options.grid(row=0, column=0, pady=8)


# Rock button
rock_btn = Button(
    input_frame,
    text='Rock',
    width=15,
    bd=0,
    bg='pink',
    pady=5,
    command=lambda: player_choice(options[0])
)
rock_btn.grid(row=1, column=1, padx=8, pady=5)


# Paper button
paper_btn = Button(
    input_frame,
    text='Paper',
    width=15,
    bd=0,
    bg='silver',
    pady=5,
    command=lambda: player_choice(options[1])
)
paper_btn.grid(row=1, column=2, padx=8, pady=5)


# Scissors button
scissors_btn = Button(
    input_frame,
    text='Scissors',
    width=15,
    bd=0,
    bg='light blue',
    pady=5,
    command=lambda: player_choice(options[2])
)
scissors_btn.grid(row=1, column=3, padx=8, pady=5)


# Score label
score_label = Label(
    input_frame,
    text='Score : ',
    font=app_font,
    fg='grey'
)
score_label.grid(row=2, column=0)


# Player choice label
player_choice_label = Label(
    input_frame,
    text='Your Selected : ---',
    font=app_font
)
player_choice_label.grid(row=3, column=1, pady=5)


# Player score label
player_score_label = Label(
    input_frame,
    text='Your Score : -',
    font=app_font
)
player_score_label.grid(row=3, column=2, pady=5)


# Computer choice label
computer_choice_label = Label(
    input_frame,
    text='Computer Selected : ---',
    font=app_font,
    fg='black'
)
computer_choice_label.grid(row=4, column=1, pady=5)


# Computer score label
computer_score_label = Label(
    input_frame,
    text='Computer Score : -',
    font=app_font,
    fg='black'
)
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)


# Set window size
game_window.geometry('700x300')

# Start the GUI event loop
game_window.mainloop()
