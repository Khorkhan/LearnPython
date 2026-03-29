import random

dmg = random.randint(10, 20)
print(f"You dealt {dmg} damage!")

#random loot
loot_table = ["Common Sword", "Rare Shield", "Legendary Essence"]
found_item = random.choice(loot_table)

print(f"You opened the chest and found: {found_item}!")