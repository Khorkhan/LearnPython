def calculate_exp(monster_level, multiplier):
    total_exp = monster_level * multiplier
    return total_exp

my_reward = calculate_exp(5, 100)

print(my_reward)