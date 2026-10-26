from tkinter import *          # Imports Tkinter (lets you make windows and graphics)
import random                  # Lets us pick random numbers
from tkinter import messagebox # Allows pop-up message windows
import time                    # Lets us slow down the game

root = Tk()                    # Creates the main game window
root.title("Pong Game")        # Sets title of the window
root.resizable(0, 0)           # Prevents the window from being resized
root.wm_attributes("-topmost", 1)  # Keeps window on top of others

# Create the game canvas (the area where the game happens)
# width=600 → 600 pixels wide
# height=500 → 500 pixels tall
canvas = Canvas(root, width=600, height=500, bd=1, highlightthickness=1)
canvas.config(bg="black")      # Make background black
canvas.pack()                  # Put the canvas inside the game window

# Score text shown at the top center
l = canvas.create_text(300, 20, font=("Arial", 20, "bold"), text=" : ", fill="white")

root.update()                  # Update window to make sure everything is shown

canvas.create_line(300, 0, 300, 600, fill="white")  
# Draw a white line in the middle for decoration (x1, y1, x2, y2)


# ---------------------- BALL CLASS ------------------------------------
class Ball:
    # Updates the score text at the top
    def update(self):
        l.configure(text=str(self.score1) + ' : ' + str(self.score2))

    # What happens when a new ball is created
    def __init__(self, canvas, paddle1, paddle2, color):
        self.paddle1 = paddle1      # Left paddle
        self.paddle2 = paddle2      # Right paddle
        self.canvas = canvas

        # Create the ball (circle)
        # (10,10,30,30) → size of the ball
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)

        self.canvas.move(self.id, 283, 300)  # Move ball near center

        # Random starting speeds
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[1]          # Random left/right speed
        self.y = starts[2]          # Random up/down speed

        self.canvas_height = self.canvas.winfo_height() # How tall the game area is
        self.canvas_width = self.canvas.winfo_width()   # How wide the game area is

        self.score1 = 0
        self.score2 = 0

    # Moves the ball every frame
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)   # Move ball
        pos = self.canvas.coords(self.id)           # Get ball position

        # Bounce off top
        if pos[1] <= 0:
            self.y = 4

        # Bounce off bottom
        if pos[3] >= self.canvas_height:
            self.y = -4

        # Ball hits left wall → Player 2 scores
        if pos[0] <= 0:
            self.x = 4
            self.score1 += 1
            canvas.itemconfigure(l, text=str(self.score1) + " : " + str(self.score2))

        # Ball hits right wall → Player 1 scores
        if pos[2] >= self.canvas_width:
            self.x = -4
            self.score2 += 1
            canvas.itemconfigure(l, text=str(self.score1) + " : " + str(self.score2))

        # Ball hits left paddle
        if self.hit_paddle1(pos) == True:
            self.x = 4

        # Ball hits right paddle
        if self.hit_paddle2(pos) == True:
            self.x = -4

    # Check if ball hits paddle1 (left paddle)
    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        # If ball is inside paddle vertical area (top to bottom)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            # If ball touches paddle horizontally
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
        return False

    # Check if ball hits paddle2 (right paddle)
    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
        return False


# ---------------------- LEFT PADDLE CLASS -----------------------------
class Paddle1:
    pos = [0, 0, 0, 0]   # Stores paddle position

    def __init__(self, canvas, color):
        self.canvas = canvas

        # Create a rectangle for paddle1
        # (10,180,25,280) → x1,y1,x2,y2
        self.id = canvas.create_rectangle(10, 180, 25, 280, fill=color)

        self.y = 0                       # Paddle movement speed (up/down)
        self.canvas_height = self.canvas.winfo_height()

        # Bind keyboard keys
        self.canvas.bind_all('a', self.turn_left)     # 'a' key moves up
        self.canvas.bind_all('d', self.turn_right)    # 'd' key moves down

    def draw(self):
        self.canvas.move(self.id, 0, self.y)          # Move paddle
        pos = self.canvas.coords(self.id)

        # Stop paddle from leaving top
        if pos[1] <= 0:
            self.y = 0

        # Stop paddle from leaving bottom
        if pos[3] >= self.canvas_height:
            self.y = 0

    def turn_left(self, event):
        self.y = -4   # Move up

    def turn_right(self, event):
        self.y = 4    # Move down


# ---------------------- RIGHT PADDLE CLASS ----------------------------
class Paddle2:
    pos = [0, 0, 0, 0]

    def __init__(self, canvas, color):
        self.canvas = canvas

        # Create paddle on the right side
        self.id = canvas.create_rectangle(575, 180, 590, 280, fill=color)

        self.y = 0
        self.canvas_height = self.canvas.winfo_height()

        # Arrow keys for Player 2
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)   # Left arrow moves down
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right) # Right arrow moves up

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)

        # Stop paddle at top
        if pos[1] <= 0:
            self.y = 0

        # Stop paddle at bottom
        if pos[3] >= self.canvas_height:
            self.y = 0

    def turn_left(self, event):
        self.y = 4    # Move DOWN

    def turn_right(self, event):
        self.y = -4   # Move UP


# ---------------------- EXTRA DECORATION ------------------------------
# Middle circle for styling
middle_circle = canvas.create_oval(10, 10, 150, 150, outline="white")
canvas.move(middle_circle, 220, 170)

# Create game objects
paddle1 = Paddle1(canvas, "orange")
paddle2 = Paddle2(canvas, "lightgreen")
ball = Ball(canvas, paddle1, paddle2, "yellow")


# ---------------------- MAIN GAME LOOP -------------------------------
while 1:
    # First to 10 points wins
    if ball.score1 == 10 or ball.score2 == 10:
        messagebox.showinfo("Game Over", "Player 1 =" + str(ball.score1) +
                            " Player 2 =" + str(ball.score2))
        break

    ball.draw()       # Move ball
    paddle1.draw()    # Move paddle 1
    paddle2.draw()    # Move paddle 2

    root.update_idletasks()
    root.update()

    time.sleep(0.01)  # Slow the game down

root.mainloop()       # Keep the window open
