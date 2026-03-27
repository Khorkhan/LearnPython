player_hp = 100
monster_attack = 25
defense = 5

final_damage = monster_attack - defense
player_hp = player_hp - final_damage

print(f"Player took {final_damage} damage. Remaining HP: {player_hp}")

critical_damage = (monster_attack * 2) - defense
print(f"If monster lands a Critical hit, damage will be {critical_damage}.")