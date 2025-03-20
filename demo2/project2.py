import os
from datetime import datetime

DIARY_FILE = "diary_entries.txt"

# Load diary entries from file
def load_entries():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

# Save diary entries to file
def save_entries(entries):
    with open(DIARY_FILE, "w") as f:
        for entry in entries:
            f.write(entry + "\n")

# Create a new diary entry
def create_entry():
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_text = input("Write your diary entry:\n")
    entry = f"{date_time} - {entry_text}"
    
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)

    print("Diary entry saved!")

# View all diary entries
def view_entries():
    entries = load_entries()
    if not entries:
        print("No diary entries found.")
    else:
        print("\n--- Your Diary Entries ---")
        for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry}")

# Edit an existing diary entry
def edit_entry():
    view_entries()
    entries = load_entries()

    if not entries:
        return

    try:
        entry_num = int(input("Enter the entry number to edit: ")) - 1
        if 0 <= entry_num < len(entries):
            new_text = input("Enter the updated entry: ")
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entries[entry_num] = f"{date_time} - {new_text}"
            save_entries(entries)
            print("Diary entry updated!")
        else:
            print("Invalid entry number!")
    except ValueError:
        print("Please enter a valid number.")

# Delete an existing diary entry
def delete_entry():
    view_entries()
    entries = load_entries()

    if not entries:
        return

    try:
        entry_num = int(input("Enter the entry number to delete: ")) - 1
        if 0 <= entry_num < len(entries):
            entries.pop(entry_num)
            save_entries(entries)
            print("Diary entry deleted!")
        else:
            print("Invalid entry number!")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    while True:
        print("\n--- Personal Diary ---")
        print("1. Create New Entry")
        print("2. View Entries")
        print("3. Edit Entry")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
