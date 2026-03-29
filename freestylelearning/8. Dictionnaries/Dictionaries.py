player = {
    "name": "Iris",
    "hp": 100,
    "level": 5
}

print(player["name"])

#changing stats
player["hp"] -= 20
player["gold"] = 50

#character sheet
def heal(target):
    target["hp"] += 20
    print(f"{target['name']} healed! Current HP: {target['hp']}")

hero = {"name": "Iris", "hp": 50}
monster = {"name": "Slime", "hp": 20}

heal(hero)