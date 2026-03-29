inventory = ["Sword" , "Shield", "Potion"]
print(inventory[0])
print(inventory[1])

#pick up item system
bag = ["Map", "Bread"]
print(f"Current bag: {bag}")

new_item = input("You fund chest! What's inside?: ")
bag.append(new_item)

print(f"Your bag now contain: ")
for item in bag:
    print(f"- {item}")