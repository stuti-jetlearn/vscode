import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import speech_recognition as sr

# Create window
Window = tk.Tk()
Window.title("Speech to Text")
Window.geometry("800x400")

# Heading
heading1 = tk.Label(Window, text="Voice Notepad", font=("Arial", 20, "bold"))
heading1.grid(row=0, column=1, padx=20, pady=20)

# Text label
Output_text = tk.Text(Window, height=4, width=40)
Output_text.grid(row=1, column=1, pady=20, padx=20)

# Function to translate speech to text
def Translate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "Sorry, could not recognize your voice"
        Output_text.delete(1.0, tk.END)
        Output_text.insert(tk.END, text)

# Function to save text
def save():
    fout = filedialog.asksaveasfile(defaultextension=".txt")
    if fout:
        fout.write(Output_text.get(1.0, tk.END))
        fout.close()
    else:
        messagebox.showinfo("Warning", "Text not saved")

# Use tk.Button instead of ttk.Button to apply font
trans_btn = tk.Button(Window, text="Click on me!..\nTo start recording",
                      font=("Arial", 15, "bold"), command=Translate, width=20)
trans_btn.grid(row=1, column=0, pady=20, padx=20)

save_button = tk.Button(Window, text="Save the Text", width=20, height=2, command=save)
save_button.grid(row=1, column=2, pady=10, columnspan=3)

# Start the GUI
Window.mainloop()
