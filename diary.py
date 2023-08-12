import os
import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("Welcome to the Easy Diary:")
    print("1. View Entries")
    print("2. Add Entry")
    print("3. Delete Entry")
    print("4. Exit")

def view_entries(entries):
    clear_screen()
    print("Diary Entries:")
    for date, entry in entries.items():
        print(f"\nDate: {date}")
        print("----")
        print(entry)
        print("----")

def add_entry(entries):
    clear_screen()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entry = input("Enter your diary entry for today:\n")
    entries[today] = new_entry
    print("Entry added successfully!\n")

def delete_entry(entries):
    clear_screen()
    date_to_delete = input("Enter the date of the entry you want to delete (YYYY-MM-DD): ")
    if date_to_delete in entries:
        confirm = input("Are you sure you want to delete this entry? (y/n): ")
        if confirm.lower() == 'y':
            del entries[date_to_delete]
            print("Entry deleted successfully!\n")
        else:
            print("Deletion canceled.\n")
    else:
        print("Entry not found.")
    

def main():
    entries = {}  # Dictionary to store diary entries

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_entries(entries)
            input("Press Enter to continue...")
        elif choice == '2':
            add_entry(entries)
            input("Press Enter to continue...")
        elif choice == '3' :
            clear_screen()
            delete_entry(entries)
            input("Press Enter to continue...")
        elif choice == '4':
            clear_screen()
            print("Goodbye!")
            break
        else:
            clear_screen()
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
