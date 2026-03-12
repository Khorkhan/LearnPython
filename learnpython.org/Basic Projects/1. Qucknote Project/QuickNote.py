def add_note():
    note = input("Enter text you want to note: ")
    with open("my_note.txt", "a", encoding="utf-8") as f:
        f.write(f"- {note}\n")
    print("Data Saved!")

def show_notes():
    print("\n--- Your note list ---")
    try:
        with open("my_note.txt", "r", encoding="utf-8") as f:
            note = f.readlines()
            if not note:
                print("No data")
            else:
                for index, line in enumerate(note, 1):
                    print(f"{index}. {line.strip()}")
    except FileExistsError:
        print("No log file has been created yet.")

def main():
    while True:
        print("\n[1] Add data [2] view all record [3] Exit")
        choice = input("Choice (1/2/3): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            print("Close program...")
            break
        else:
            print("Please select 1, 2, or 3 only")

if __name__ == "__main__":
    main()