from tkinter import *
from tkinter.ttk import *

# Creating tkinter window 
window = Tk() 
window.title('Simple Calculator')

# Entry widget to display expressions
expression = ""
entry_text = StringVar()
entry = Entry(window, textvariable=entry_text, width=25, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)

# Function to evaluate expression
def equal_press():
    try:
        global expression
        result = str(eval(expression))
        entry_text.set(result)
        expression = ""
    except:
        entry_text.set("Error")
        expression = ""

# Function to clear entry
def clear():
    global expression
    expression = ""
    entry_text.set("")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Creating and placing buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = Button(window, text=text, command=equal_press, width=5)
    else:
        btn = Button(window, text=text, command=lambda t=text: press(t), width=5)
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = Button(window, text='C', command=clear, width=5)
clear_button.grid(row=5, column=0, columnspan=4, pady=5)

window.mainloop()
