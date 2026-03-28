hp = 0

if hp <= 0:
    print("You have fallen in battle...")
    print("Game over")
else:
    print("You are still standing!")

level = int(input("Enter your level: "))

if level >= 50:
    print("You can enter the Holy Throne.")
elif level >= 10:
    print("You can enter the Cathedral.")
else:
    print("You are too weak. Go train in the Woods!")

#Exercise
character_name = input("Enter your character name: ")
current_hp = int(input("Enter your current HP: "))

#check condition
if current_hp == 0:
    print(f"{character_name} has died.")
elif current_hp < 20:
    print(f"Warning: Low HP, {character_name} drink a potion!")
else:
    print(f"{character_name}, you are ready or adventure!")