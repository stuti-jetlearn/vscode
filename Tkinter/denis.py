from tkinter import *
import calender

screen = Tk()
screen.geometry("250x200")
screen.config(background = "Red")

#labels
cal = Label(screen, text = "Calender", font = ("Courgette", 40), bg = "blue")
cal.place(x = 40, y = 5)
year = Label(screen, text = "Enter Year", font = ("Courgette", 20), bg = "orange")
year.place(x = 65, y = 60)
#entry
cale = Entry(screen, width = 15)
cale.place(x = 50, y = 90 )
#button
calend = Button(screen, text = "Show Calender", bg = "yellow", font = ("courgette", 20))
calend.place(x = 50, y = 120)
exit = Button(screen, text = "Exit", font = ("courgette", 20))
exit.place(x = 80, y = 160)




screen.mainloop()