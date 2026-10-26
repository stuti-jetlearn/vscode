from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.title("Multiply")

# Define style for labels and button
style = Style()
style.configure("TLabel", font=("Arial", 15))
style.configure("TButton", font=("Arial", 15))
style.configure("TCombobox", font=("Arial", 12))

# Labels
label1 = Label(screen, text="Mathematical Table", style="TLabel")
label2 = Label(screen, text="Number and range:", style="TLabel")
label1.grid(row=0, column=0, columnspan=3, pady=20)
label2.grid(row=1, column=0, padx=30)

# Combobox
number = IntVar()
combo = Combobox(screen, textvariable=number)
combo['values'] = tuple(range(101))
combo.grid(row=1, column=1)

# Button
button1 = Button(screen, text="Enter", style="TButton")
button1.grid(row=2, column=1, pady=10)

screen.mainloop()
