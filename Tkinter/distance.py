from tkinter import *
import tkinter.font as font

def calculate_distance():
    try:
        time = float(time_entry.get())  # Get time input
        speed = float(speed_entry.get())  # Get speed input
        distance = time * speed  # Calculate distance
        result_label.config(text=f"Distance Covered: {distance:.2f} units")  
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

# Create main window
root = Tk()
root.title("Distance Calculator")
root.geometry("400x300")

# Set font style
app_font = font.Font(size=12)

# Title Label
title_label = Label(root, text="Distance Calculator", font=font.Font(size=16, weight="bold"), fg="blue")
title_label.pack(pady=10)

# Time Input
time_label = Label(root, text="Enter Time (hours):", font=app_font)
time_label.pack()
time_entry = Entry(root, font=app_font)
time_entry.pack(pady=5)

# Speed Input
speed_label = Label(root, text="Enter Speed (units/hr):", font=app_font)
speed_label.pack()
speed_entry = Entry(root, font=app_font)
speed_entry.pack(pady=5)

# Calculate Button
calculate_btn = Button(root, text="Calculate Distance", font=app_font, bg="lightblue", command=calculate_distance)
calculate_btn.pack(pady=10)

# Result Label
result_label = Label(root, text="Distance Covered: ---", font=app_font, fg="green")
result_label.pack(pady=5)

# Run the application
root.mainloop()
