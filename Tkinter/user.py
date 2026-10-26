from tkinter import *

def save_details():
    username = user_name_input_area.get()
    password = user_password_entry_area.get()
    
    # Simple file handling
    with open("user_details.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")
    
    # Optional: clear the fields
    user_name_input_area.delete(0, END)
    user_password_entry_area.delete(0, END)

top = Tk()
top.title("Login Me")
top.geometry("450x300")
top.config(background="pink")

# the label for user_name
Label(top, text="Username").place(x=40, y=60)

# the label for user_password
Label(top, text="Password").place(x=40, y=100)

# input areas (save references)
user_name_input_area = Entry(top, width=30)
user_name_input_area.place(x=110, y=60)

user_password_entry_area = Entry(top, show='*', width=30)
user_password_entry_area.place(x=110, y=100)

# submit button
Button(top, text="Submit", command=save_details).place(x=40, y=130)

top.mainloop()
