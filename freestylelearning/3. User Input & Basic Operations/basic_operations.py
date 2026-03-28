#receive player name
player_name = input("Enter your name, Traveler: ")
print(f"Welcome to the Shop, {player_name}!")

#receive potion
potion_count = input("How many potions do you want to buy? ")
potion_count = int(potion_count)

#calculate price
total_price = potion_count * 20
print(f"That will be {total_price} gold, please.")

#Exercise
base_damage = int(input("Enter your base damage: "))
multiplier = float(input("Enter your damage multiplier: "))
final_dmg = base_damage * multiplier
print(f"Your total damage is {final_dmg} point!")