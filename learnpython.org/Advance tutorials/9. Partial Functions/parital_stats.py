from functools import partial

def calc_power(base_atk, multiplier):
    return base_atk * multiplier

orc_power = partial(calc_power, multiplier = 1.5)
human_power = partial(calc_power, multiplier = 1.0)

print("Orc power: ", orc_power(100))
print("Human Power: ", human_power(100))