"""
This file handles user registration and login.
"""

import hashlib
from storage import load_users, save_users


def hash_password(password):
    """Convert a password into a secure hash."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(username, password):
    """Create a new user account."""
    users = load_users()

    for user in users:
        if user["username"] == username:
            return False, "Username already exists."

    users.append({
        "username": username,
        "password_hash": hash_password(password)
    })
    save_users(users)
    return True, "Account created successfully."


def authenticate_user(username, password):
    """Check if the login details are correct."""
    users = load_users()
    password_hash = hash_password(password)

    for user in users:
        if user["username"] == username and user["password_hash"] == password_hash:
            return True

    return False


def login_or_register():
    """Show the login menu and let the user log in or register."""
    while True:
        print("\n========== LOGIN ==========")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if authenticate_user(username, password):
                print(f"Welcome, {username}!")
                return username
            else:
                print("Invalid username or password.")

        elif choice == "2":
            username = input("Choose a username: ").strip()
            password = input("Choose a password: ").strip()

            success, message = register_user(username, password)
            print(message)

        elif choice == "3":
            return None

        else:
            print("Invalid choice.")