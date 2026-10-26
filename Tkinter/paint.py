# Import everything from tkinter (GUI library)
from tkinter import *

# Import color chooser dialog
from tkinter.colorchooser import askcolor  

# ---------- Default settings ----------

# Default thickness of pen/brush
DEFAULT_PEN_SIZE = 5.0  

# Default drawing color
DEFAULT_COLOR = 'black'  

# ---------- Global variables ----------

# Store previous mouse coordinates for drawing continuous lines
old_x = None  
old_y = None  

# Current drawing color
color = DEFAULT_COLOR  

# Flag to check if eraser is active
eraser_on = False  

# Store currently active tool button
active_button = None  

# Line width (initially default)
line_width = DEFAULT_PEN_SIZE  

# ---------- Functions ----------

# Activate pen tool
def use_pen():
    global active_button, eraser_on
    activate_button(pen_button)  # Highlight pen button
    eraser_on = False  # Disable eraser


# Activate brush tool
def use_brush():
    global active_button, eraser_on
    activate_button(brush_button)  # Highlight brush button
    eraser_on = False  # Disable eraser


# Open color picker dialog
def choose_color():
    global color, eraser_on
    eraser_on = False  # Disable eraser
    picked_color = askcolor(color=color)[1]  # Get selected color (hex value)
    if picked_color:  # If user selected a color
        color = picked_color  # Update current color


# Activate eraser tool
def use_eraser():
    global eraser_on
    activate_button(eraser_button)  # Highlight eraser button
    eraser_on = True  # Enable eraser


# Handle button activation (UI effect)
def activate_button(some_button):
    global active_button
    if active_button:  # If some button is already active
        active_button.config(relief=RAISED)  # Reset its appearance
    some_button.config(relief=SUNKEN)  # Highlight selected button
    active_button = some_button  # Set new active button


# Drawing function (called when mouse moves with button pressed)
def paint(event):
    global old_x, old_y, color

    size = choose_size_button.get()  # Get size from slider

    # If brush tool is active, make it thicker
    if active_button == brush_button:
        width = size * 2
    else:
        width = size

    # If eraser is active, draw in white; otherwise use selected color
    paint_color = 'white' if eraser_on else color  

    # Draw line only if previous coordinates exist
    if old_x and old_y:
        c.create_line(old_x, old_y, event.x, event.y,
                      width=width, fill=paint_color,
                      capstyle=ROUND, smooth=TRUE, splinesteps=36)

    # Update previous coordinates
    old_x, old_y = event.x, event.y  


# Reset coordinates when mouse button is released
def reset(event):
    global old_x, old_y
    old_x, old_y = None, None  


# ---------- UI setup ----------

# Create main window
root = Tk()  

# Set window title
root.title("Simple Paint App")  

# Create Pen button
pen_button = Button(root, text='Pen', command=use_pen)
pen_button.grid(row=0, column=0)  

# Create Brush button
brush_button = Button(root, text='Brush', command=use_brush)
brush_button.grid(row=0, column=1)  

# Create Color picker button
color_button = Button(root, text='Color', command=choose_color)
color_button.grid(row=0, column=2)  

# Create Eraser button
eraser_button = Button(root, text='Eraser', command=use_eraser)
eraser_button.grid(row=0, column=3)  

# Create slider to choose size (1 to 10)
choose_size_button = Scale(root, from_=1, to=10, orient=HORIZONTAL)
choose_size_button.grid(row=0, column=4)  

# Create drawing canvas
c = Canvas(root, bg='white', width=600, height=600)
c.grid(row=1, columnspan=5)  

# ---------- Bindings ----------

# Bind mouse drag (left button) to paint function
c.bind('<B1-Motion>', paint)  

# Bind mouse release to reset function
c.bind('<ButtonRelease-1>', reset)  

# ---------- Start defaults ----------

# Set default tool as pen
activate_button(pen_button)  

# Run the application
root.mainloop()  