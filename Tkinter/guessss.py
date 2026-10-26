from tkinter import *
import tkinter.font as font
import random

# Initialize game variables
secret_number = random.randint(1, 100)
attempts = 0

# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            result_label.config(text="Too Low! Try Again.")
        elif guess > secret_number:
            result_label.config(text="Too High! Try Again.")
        else:
            result_label.config(text=f"Correct! You guessed it in {attempts} tries.")
            submit_button.config(state=DISABLED)
            guess_entry.config(state=DISABLED)
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Function to reset the game
def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Game reset! Guess a number between 1 and 100.")
    guess_entry.delete(0, END)
    submit_button.config(state=NORMAL)
    guess_entry.config(state=NORMAL)

# Create main window
root = Tk()
root.title("Number Guessing Game")
root.geometry("500x300")

# Fonts
app_font = font.Font(size=12)

# Title
title_label = Label(root, text="Guess the Number (1-100)", font=font.Font(size=20), fg="darkblue")
title_label.pack(pady=10)

# Result message
result_label = Label(root, text="Guess a number between 1 and 100.", font=app_font)
result_label.pack(pady=5)

# Entry for user guess
guess_entry = Entry(root, font=app_font, width=10, justify='center')
guess_entry.pack(pady=5)

# Submit button
submit_button = Button(root, text="Submit Guess", font=app_font, command=check_guess, bg="lightgreen")
submit_button.pack(pady=5)

# Reset button
reset_button = Button(root, text="Reset Game", font=app_font, command=reset_game, bg="lightcoral")
reset_button.pack(pady=5)

root.mainloop()
