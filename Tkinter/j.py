# Importing required modules
import tkinter                 # tkinter module for GUI
from tkinter import *          # Import everything from tkinter
import random                  # For generating random numbers
from tkinter import messagebox # For showing popup messages

# Creating the main window
root = tkinter.Tk()

# Lists of correct words and their jumbled versions
answers = ["apple", "mango", "banana", 'achieve', 'kolkata', 'evening', 'servant', 'receiver', 
           'london', 'ferrari', 'hollow', 'horror', 'master', 'morning', 'bottle', 'pen', 
           'router', 'copy', 'narrow', 'wide', 'dive', 'love', 'block', 'right', 'simple', 
           'deaf', 'single', 'knight', 'hope']
words = ['plpea', 'gnoma', 'annaba', 'hveeica', 'lkaatko', 'egvnine', 'aestnrv', 'iceever', 
         'lndono', 'rrreifa', 'wllhoo', 'oohrrr', 'rtemsa', 'nnrgimo', 'lttobe', 'enp', 
         'ourrte', 'ypco', 'rraonw', 'wdie', 'ievd', 'elov', 'klboc', 'ightr', 'plmsie', 
         'dfea', 'glneis', 'ghtkni', 'opeh']

# Select a random index for the first word
num = random.randrange(0, len(words), 1)

# Initialize score and attempts
c = 0  # Correct answers count
d = 0  # Total attempts
s = "" # Score string to be displayed
l = Label(root)  # Placeholder label for score display

# Function to reset the word and input box
def reset():
    global words, answers, num
    num = random.randrange(0, len(words), 1)      # Pick a new random word
    label.config(text = words[num])               # Update the label to show jumbled word
    e1.delete(0, END)                             # Clear the input box

# Function to set the first word when game starts
def default():
    global words, answers, num
    label.config(text = words[num])               # Show the initial jumbled word

# Function to check the user's answer
def checkans():
    global words, answers, num, c, d, s, l
    d = int(d) + 1                                 # Increment total attempts
    var = e1.get()                                 # Get the user's input
    if var == answers[num]:                        # Check if input is correct
        messagebox.showinfo("Congratulations", "It's the correct answer!!")
        c = int(c) + 1                             # Increment correct count
    else:
        messagebox.showerror("Sorry", "It's not the correct answer.")
    s = 'Score :' + str(c) + '/' + str(d)          # Update score text
    l.forget()                                     # Remove old score label
    l = Label(root, font=("Verdana", 20), text=s, bg="#000000", fg="#fff")
    l.pack(side=LEFT)                              # Show updated score
    reset()                                        # Pick a new word

# Set window size and position
root.geometry("500x500+500+150")                   # Width x Height + Xpos + Ypos

# Set window title and background color
root.title("Jumbled word game")
root.configure(background="#000000")

# Heading of the game
Label(root, text="JUMBLED WORD GAME", font=("Verdana", 28), bg="#000000", fg="#fff").pack(pady=5)

# Label where the jumbled word will be shown
label = Label(root, font=("Verdana", 22), bg="#000000", fg="#fff")
label.pack(pady=30, ipady=10, ipadx=10)

# Entry box for user input
ans = StringVar()                                   # Define a string variable to link with Entry
e1 = Entry(root, font=("Verdana", 20), textvariable=ans)
e1.pack(ipady=5, ipadx=5)                           # ipady and ipadx are internal paddings

# Check button to submit answer
Button(root, text="Check", font=("Comic sans ms", 20), width=10,
       bg="#333945", fg="#45CE30", relief=GROOVE, command=checkans).pack(pady=40)

# Reset button to skip word and try a new one
Button(root, text="Reset", font=("Comic sans ms", 20), width=10,
       bg="#777E8B", fg="#E1DA00", relief=GROOVE, command=reset).pack()

# Set the first jumbled word on screen
default()

# Start the main event loop of the GUI
root.mainloop()
