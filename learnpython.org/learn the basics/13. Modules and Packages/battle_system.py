import random

def get_damage(base_atk):
    bonus = random.randint(1, 10)
    return base_atk + bonus

print(get_damage(50))
print(get_damage(50))
print(get_damage(50))