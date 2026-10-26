from tkinter import *
from tkinter.filedialog import *

screen = Tk()
screen.title("Open/Delete file")

# Frame to hold all buttons horizontally
button_frame = Frame(screen)
button_frame.pack(side=TOP, anchor='w', padx=10, pady=5)

# Add buttons inside the frame
save = Button(button_frame, text="Save")
save.pack(side=LEFT, padx=5)

add = Button(button_frame, text="Add")
add.pack(side=LEFT, padx=5)

open_btn = Button(button_frame, text="Open")  # 'open' is a built-in function, avoid overwriting it
open_btn.pack(side=LEFT, padx=5)

delete = Button(button_frame, text="Delete")
delete.pack(side=LEFT, padx=5)

# Entry box below the buttons
entry = Entry(screen, width=30)
entry.pack(side=TOP, anchor='w', padx=10, pady=5)

# Listbox and scrollbar on the right
frame = Frame(screen)
scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, width=50, yscrollcommand=scrollbar.set, bg="gray")
for i in range(100):
    listbox.insert(END, "file" + str(i))
listbox.pack(side=RIGHT, padx=5)

scrollbar.config(command=listbox.yview)
frame.pack(side=RIGHT)

screen.mainloop()
