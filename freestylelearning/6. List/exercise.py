my_essence = ["Fire Essence"]
print("Your bag contains: ", my_essence)

remove_item = input("Which item you want to drop? ")
my_essence.remove(remove_item)

new_item = input("Which item you want to pick up? ")
my_essence.append(new_item)

print("Your bag now contains: ", my_essence)