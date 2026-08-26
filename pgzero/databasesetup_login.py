import sqlite3

# This is the database file used by the project.
DATABASE = "internalassessment_login.db"


def setup_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Existing table: stores all the Spanish words used by the game.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        spanish_word TEXT NOT NULL,
        translation TEXT NOT NULL,
        difficulty INTEGER NOT NULL
    )
    """)

    # NEW TABLE FOR SIGN UP / LOGIN
    # Each learner gets one account.
    # username is UNIQUE so two accounts cannot use the same username.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    # Existing player table, now linked to a user account.
    # user_id connects the game player to the account that logged in.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT NOT NULL,
        level INTEGER DEFAULT 1,
        games_played INTEGER DEFAULT 0,
        games_won INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    # Stores the result of each game.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS game_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id INTEGER,
        word_id INTEGER,
        won INTEGER,
        guesses_used INTEGER,
        FOREIGN KEY (player_id) REFERENCES players(id),
        FOREIGN KEY (word_id) REFERENCES words(id)
    )
    """)

    connection.commit()
    connection.close()


def signup(name, username, password):
    # This function saves the information entered on the Sign Up page.
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (name, username, password)
        VALUES (?, ?, ?)
        """, (name, username, password))

        # commit() permanently saves the new user in the database.
        connection.commit()

        # Get the ID of the newly created user.
        user_id = cursor.lastrowid

        # Create a player record for this user so game progress can
        # be connected to the account.
        cursor.execute("""
        INSERT INTO players (user_id, name)
        VALUES (?, ?)
        """, (user_id, name))

        connection.commit()

        return True, "Account created successfully!"

    except sqlite3.IntegrityError:
        # This happens if the username already exists.
        return False, "Username already exists."

    finally:
        connection.close()


def login(username, password):
    # This function checks the username and password entered
    # on the Login page.
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id, name
    FROM users
    WHERE username = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()
    connection.close()

    if user:
        # Returns the user's ID and name if login is successful.
        return True, user[0], user[1]
    else:
        return False, None, None


def save_game_result(user_id, word_id, won, guesses_used):
    # This function saves the result of a completed game.
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Find the player belonging to the logged-in user.
    cursor.execute("""
    SELECT id
    FROM players
    WHERE user_id = ?
    """, (user_id,))

    player = cursor.fetchone()

    if player:
        player_id = player[0]

        # Save the game result.
        cursor.execute("""
        INSERT INTO game_results
        (player_id, word_id, won, guesses_used)
        VALUES (?, ?, ?, ?)
        """, (player_id, word_id, won, guesses_used))

        # Update the player's statistics.
        cursor.execute("""
        UPDATE players
        SET games_played = games_played + 1,
            games_won = games_won + ?
        WHERE id = ?
        """, (won, player_id))

        connection.commit()

    connection.close()


# Run this once to make sure all required tables exist.
setup_database()
print("Database setup complete.")
