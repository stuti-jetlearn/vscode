import pgzrun       # Import Pygame Zero module to create games
import random       # Import random module to select items randomly

# --- Game Window Settings ---
HEIGHT = 630        # Set window height
WIDTH = 1100        # Set window width

# --- Game State Variables ---
gameo = False       # Flag to indicate if the player lost
gamec = False       # Flag to indicate if the player won
level = 1           # Current level of the game
l2 = []             # List of current falling Actor objects
tlev = 8            # Total number of levels
speed = 9           # Base speed for falling items
l1 = ["bag.png", "computer.png", "mirror.png", "pot.png"]  # List of possible items
target_item = None  # The item the player must click this round

# --- Draw Function ---
def draw():
    screen.blit("recycle.jpg", (0, 0))  # Draw the background image at top-left corner

    if gameo:  # If player lost
        screen.draw.text("You Lost!", center=(550, 150), fontsize=60, color="black")  # Show message
        screen.draw.text("Click to Restart", center=(550, 230), fontsize=40, color="black")  # Show restart prompt

    elif gamec:  # If player won
        screen.draw.text("You Won!", center=(550, 150), fontsize=60, color="black")  # Show message
        screen.draw.text("Click to Restart", center=(550, 230), fontsize=40, color="black")  # Show restart prompt

    else:  # Game is ongoing
        for t in l2:       # Draw all falling items
            t.draw()
        # Display current level at top-left
        screen.draw.text(f"Level: {level}", topleft=(20, 20), fontsize=40, color="black")
        # Display the target item to click at the top center
        if target_item:
            # Remove file extension and capitalize first letter
            screen.draw.text(f"Click the {target_item.split('.')[0].capitalize()}!", 
                             midtop=(WIDTH//2, 20), fontsize=50, color="black")

# --- Update Function ---
def update():
    global l2, level
    if gameo or gamec:   # Stop updating if game over or won
        return
    if len(l2) == 0:     # If no items on screen, start a new round
        l2 = put(level)

# --- Function to create falling items ---
def put(extra):
    global target_item
    l3 = []  # Temporary list to hold actors for this round
    target_item = random.choice(l1)  # Randomly select one item as the target
    # Select 'extra' wrong items randomly from remaining items
    wrong_items = random.choices([i for i in l1 if i != target_item], k=extra)
    option = [target_item] + wrong_items  # Combine target + wrong items
    random.shuffle(option)                 # Shuffle so target is not always first

    size = WIDTH / (len(option) + 1)      # Horizontal spacing between items
    for u, img in enumerate(option):
        act = Actor(img)                   # Create Actor object for this image
        act.active = True                  # Mark actor as active (for game logic)
        act.x = (u + 1) * size             # Set x-position
        act.y = random.randint(-100, 0)    # Random y-position above the screen
        l3.append(act)                     # Add actor to temporary list
        # Animate the actor to fall down
        animate(
            act,
            duration=max(1, speed - level),   # Duration decreases as level increases
            on_finished=lambda a=act: reached_bottom(a),  # Call function when it reaches bottom
            y=HEIGHT
        )
    return l3  # Return the list of actors for this round

# --- Called when an actor reaches the bottom ---
def reached_bottom(actor):
    global gameo
    if not actor.active:   # Ignore if actor is no longer active (clicked or cleared)
        return
    if actor.image == target_item:  # If target item reaches bottom unclicked
        gameo = True                # Player loses

# --- Called when wrong item is clicked ---
def handle_game_over():
    global gameo
    gameo = True  # Set game over flag

# --- Called when mouse is clicked ---
def on_mouse_down(pos):
    global l2, level, gamec, gameo
    if gameo or gamec:         # If game ended, restart on click
        restart_game()
        return

    for i in l2:                # Check which item was clicked
        if i.collidepoint(pos): # If mouse clicked on this actor
            if i.image == target_item:   # Correct item clicked
                if level == tlev:        # If last level
                    gamec = True         # Player wins
                else:
                    level += 1           # Go to next level
                    # Deactivate all current actors to stop old animations
                    for a in l2:
                        a.active = False
                    l2 = []               # Clear screen for next round
            else:                        # Wrong item clicked
                handle_game_over()       # Player loses

# --- Restart the game ---
def restart_game():
    global gameo, gamec, level, l2, target_item
    for a in l2:         # Deactivate existing actors
        a.active = False
    gameo = False        # Reset game over flag
    gamec = False        # Reset game complete flag
    level = 1            # Reset level
    l2 = []              # Clear falling items
    target_item = None   # Reset target item

# --- Start the game ---
pgzrun.go()
