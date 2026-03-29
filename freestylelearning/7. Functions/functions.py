#define
def cast_fireball():
    print("Casting Fireball!")
    print("Damage dealt: 50")

cast_fireball()

#parameters
def attack(target, damage):
    print(f"Attacking! {target} for {damage} damage!")

attack("Slime", 20)

#return
def calculate_exp(base_xp, multiplier):
    return base_xp * multiplier

total_xp = calculate_exp(100, 1.5)
print(f"You gained {total_xp} EXP!")

#Victory_display
def show_status(name, hp, items):
    print("-" * 20)
    print(f"Name: {name}")
    print(f"HP: {hp}")
    print(f"items: {items}")
    print("-" * 20)

show_status("Iris", 100, ["Fire essence"])
show_status("Boss", 500, ["Darkness"])