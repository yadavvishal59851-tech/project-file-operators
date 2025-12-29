from datetime import datetime
FILENAME = "journal.txt"
def add_entry():
    try:
        message = input("Write your journal entry: ")
        time = datetime.now().strftime("%d-%m-%Y %H:%M")
        f = open(FILENAME, "a")
        f.write(time + " -> " + message + "\n")
        f.close()
        print("Today was productive day and i learn about file operators in python")
        print("Entry saved successfully")
    except Exception as e:
        print("Error : ", e)
def view_entries():
    try:
        f = open(FILENAME, "r")
        data = f.read()
        f.close()
        if data.strip() == "":
            print("No entries found")
        else:
            print("\n--- Journal Entries ---")
            print(data)
    except FileNotFoundError:
        print("Journal file not found.")
def search_entry():
    try:
        word = input("Enter word to search: ")
        f = open(FILENAME, "r")
        lines = f.readlines()
        f.close()
        found = 0
        for line in lines:
            if word in line:
                print(line.strip())
                found += 1
            if found == 0:
                print("No matching entry found.")
    except FileNotFoundError:
        print("Journal file not found.")
def delete_all():
    try:
        choice = input("Delete all entries(yes/no): ")
        if choice == "yes":
            open(FILENAME, "w").close()
            print("All entries deleted.")
        else:
            print("Delete cancelled.")
    except Exception as e:
        print("Error : ", e)
print("=== Personal Journal App ===")

while True:
    print("\n1. Add Entry")
    print("2. View Entries")
    print("3. Search Entry")
    print("4. Delete All")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter valid number!")
        continue
    if choice == 1:
        add_entry()
    elif choice == 2:
        view_entries()
    elif choice == 3:
        search_entry()
    elif choice == 4:
        delete_all()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
