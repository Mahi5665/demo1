import os
import pickle
import getpass

# File to store user credentials
USER_DB = "users.pkl"

# Load existing users
def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "rb") as f:
            return pickle.load(f)
    return {}

# Save users to file
def save_users(users):
    with open(USER_DB, "wb") as f:
        pickle.dump(users, f)

# User signup
def signup():
    users = load_users()
    username = input("Create a username: ")
    
    if username in users:
        print("Username already exists! Try logging in.")
        return
    
    password = getpass.getpass("Create a password: ")
    users[username] = password
    save_users(users)
    
    print("Account created successfully! You can now log in.")

# User login
def login():
    users = load_users()
    username = input("Enter username: ")
    
    if username not in users:
        print("Username not found! Please sign up first.")
        return None
    
    password = getpass.getpass("Enter password: ")
    
    if users[username] == password:
        print("Login successful! Welcome,", username)
        return username
    else:
        print("Incorrect password! Try again.")
        return None

# Function to create or edit a note
def write_note():
    filename = input("Enter note name (without extension): ") + ".txt"
    with open(filename, "w") as f:
        content = input("Write your note:\n")
        f.write(content)
    print("Note saved successfully!")

# Function to view a note
def read_note():
    filename = input("Enter note name to open (without extension): ") + ".txt"
    
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print("\n---- Your Note ----\n")
            print(f.read())
    else:
        print("Note not found!")

# Function to delete a note
def delete_note():
    filename = input("Enter note name to delete (without extension): ") + ".txt"
    
    if os.path.exists(filename):
        os.remove(filename)
        print("Note deleted successfully!")
    else:
        print("Note not found!")

# Main menu after login
def notepad_menu():
    while True:
        print("\n--- Notepad Menu ---")
        print("1. Create/Edit a Note")
        print("2. Read a Note")
        print("3. Delete a Note")
        print("4. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            write_note()
        elif choice == "2":
            read_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Please try again.")

# Main function
def main():
    while True:
        print("\n--- Welcome to Secure Notepad ---")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            signup()
        elif choice == "2":
            user = login()
            if user:
                notepad_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
