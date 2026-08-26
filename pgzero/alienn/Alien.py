import pgzrun
from random import randint

TITLE = "Good Shot"
WIDTH = 500
HEIGHT = 450

message = ""
alien = Actor('alien')

def draw():
    screen.clear()
    screen.fill(color=(128, 0, 0))
    alien.draw()
    screen.draw.text(message, center=(250, 30), fontsize=30, color="white")

def place_alien():
    alien.x = randint(50, WIDTH - 50)
    alien.y = randint(50, HEIGHT - 50)
    # schedule "missed" if not clicked in 2 sec
    clock.schedule_unique(missed, 2.0)

def missed():
    global message
    message = "You missed"
    place_alien()

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot"
        clock.unschedule(missed)  # cancel "missed" event
        place_alien()
    else:
        message = "You missed"

place_alien()
pgzrun.go()
