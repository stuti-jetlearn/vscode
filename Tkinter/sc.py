import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

text = tk.Text(root)
text.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=text.yview,
    bg="lightblue",          # background
    troughcolor="lightgray", # track color
    activebackground="blue"  # when clicked
)

scrollbar.pack(side="right", fill="y")

text.config(yscrollcommand=scrollbar.set)

root.mainloop()
