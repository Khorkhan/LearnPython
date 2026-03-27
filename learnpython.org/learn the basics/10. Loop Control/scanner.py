mobs = ["Slime", "Slime", "Boss", "Slime", "NPC"]

for mob in mobs:
    if mob == "NPC":
        continue

    if mob == "Boss":
        print("BOSS DETECTED! ESCAPING...")
        break
    else:
        print(f"Fighting {mob}...")