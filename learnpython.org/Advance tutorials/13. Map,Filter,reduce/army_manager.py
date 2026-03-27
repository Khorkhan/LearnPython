monster_atks = [10, 25, 40, 50, 15, 60]
strong_monters = list(filter(lambda atk: atk > 30, monster_atks))
buffed_atks = list(map(lambda atk: atk * 2, monster_atks))

print("Strong Monsters: ", strong_monters)
print("Buffed Attacks: ", buffed_atks)