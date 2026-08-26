import pgzrun                 # Import Pygame Zero to run the game
from random import randint    # Import randint to place satellites randomly
from time import time         # Import time to track how long the player takes

# Set the window size
WIDTH = 800                   # Width of the window
HEIGHT = 600                  # Height of the window

# Lists and variables to store game state
satellites = []               # Stores all satellite Actor objects
lines = []                    # Stores the line connections between satellites
next_satellite = 0            # Index of the next satellite the player must click

# Time tracking variables
start_time = 0                # When the game started
total_time = 0                # Time taken so far
end_time = 0                  # Not used here but reserved for when game ends

number_of_satellite = 8       # Total satellites to be created

# Function to create all satellites at random positions
def create_satellites():
    global start_time          # We’re going to modify start_time
    for count in range(0, number_of_satellite):  # Loop to create each satellite
        satellite = Actor("satellite")           # Create a satellite Actor from the image file named "satellite"
        satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)  # Random x,y position within window borders
        satellites.append(satellite)             # Add the satellite to the list
    start_time = time()                          # Start the timer when satellites are created

# Function that Pygame Zero calls to draw everything each frame
def draw():
    global total_time            # We’re going to update total_time

    screen.blit("background", (0,0))    # Draw background image at (0,0)

    number = 1                   # Number label to show on each satellite
    for satellite in satellites: # Loop through each satellite
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))  # Draw the number just below the satellite
        satellite.draw()         # Draw the satellite Actor
        number = number + 1      # Increment the number label

    for line in lines:           # Loop through each line in the list
        screen.draw.line(line[0], line[1], (255,255,255))  # Draw a white line between two points

    # Show timer on the screen
    if next_satellite < number_of_satellite:       # If game still going
        total_time = time() - start_time           # Calculate how long the player has been playing
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)  # Draw time in top-left
    else:                                          # If all satellites are clicked
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)  # Show the final time

# We’re not animating anything, so leave update empty
def update():
    pass  # This runs every frame, but we don’t need it now

# Function that runs when the mouse is clicked
def on_mouse_down(pos):
    global next_satellite, lines   # We’re going to change these variables

    # Check if we still have satellites left to click
    if next_satellite < number_of_satellite:
        # Check if the player clicked the correct (next) satellite
        if satellites[next_satellite].collidepoint(pos):
            # If not the first satellite, draw a line from the previous to the current one
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            # Move to the next satellite
            next_satellite = next_satellite + 1
        else:
            # Wrong satellite clicked → reset lines and start over
            lines = []
            next_satellite = 0

# Create the satellites at the start of the game
create_satellites()

# Start the Pygame Zero loop
pgzrun.go()    # Runs the game
