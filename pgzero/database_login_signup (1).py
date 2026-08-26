import sqlite3

# This is the database used by the Sign Up, Log In and Wordle program.
DATABASE = "internalassessment_login_signup.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Existing table used by the Wordle game.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        spanish_word TEXT NOT NULL,
        translation TEXT NOT NULL,
        difficulty INTEGER NOT NULL
    )
    """)

    # New table used by the Sign Up and Log In pages.
    # Each learner has a unique username and a password.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def signup(username, password):
    # Save a new learner's username and password.
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:
        cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """, (username, password))

        # commit() saves the new account permanently in the database.
        connection.commit()

        return True, "Sign up successful!"

    except sqlite3.IntegrityError:
        # This occurs when the username is already in the database.
        return False, "Username already exists."

    finally:
        connection.close()


def login(username, password):
    # Check whether the entered username and password exist together.
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id, username
    FROM users
    WHERE username = ? AND password = ?
    """, (username, password))

    user = cursor.fetchone()
    connection.close()

    if user:
        # Login was successful.
        return True, user[0], user[1]

    # Login failed.
    return False, None, None


# Create the tables when this file is run.
create_database()
print("Database is ready.")
