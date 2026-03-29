hp = 30swing
while hp > 0:
    print(f"Still Alive! HP: {hp} ")
    hp -= 10
print("You are dead.")

for i in range (3):
    print("Arrow fired!")

command = ""
print("Type 'swing' to practice or 'quit' to rest")

while command != "quit":
    command = input("> ")
    if command == "swing":
        print("You are swing your sword! (EXP + 1)")
    elif command == "quit":
        print("Taking a break...")
    else:
        print("Unknown command.")