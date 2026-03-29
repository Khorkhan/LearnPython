boss_hp = 50

while boss_hp > 0:
    print(f"Boss HP: {boss_hp}")
    input("Press Enter to attack!")
    boss_hp -= 15

print("Boss Defeated! You earned the Keeper Essence!")