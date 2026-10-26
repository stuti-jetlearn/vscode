from tkinter import *
from tkinter.ttk import*

screen = Tk()
screen.title("Main Menu")
men = Menu(screen)
files = Menu(men, tearoff = 0)
men.add_cascade(label = "file", menu = files)
files.add_command(label = "new file", command = None)
files.add_command(label = "open folder", command = None)
files.add_command(label = "close folder", command = None)
files.add_command(label = "open recent", command = None)
screen.config(menu = men)
screen.mainloop()