# import everything from tkinter module
0

# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('100x100')

# Create a Button
btn = Button(root, text='Click me !', bd='5',background="cyan",command=root.destroy)

# Set the position of button on the top of window.
#try side = bottom, right, left

btn.pack(side='top')

root.mainloop()