import random

def attack_monster(base_dmg):
    chance = random.randint(1, 10)
    if chance > 7:
        final_dmg = base_dmg * 2
        print("Critical hit!")
    else:
        final_dmg = base_dmg
        print("Normal Attack")
    return final_dmg

result = attack_monster(20)
print(f"Damage dealt: {result}")