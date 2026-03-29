monster = {
    "name": "Goblin",
    "hp": 80,
    "exp_reward": 150
}

print(f"A wild {monster['name']} appeared!")

monster["hp"] -= 30

print(f"{monster['name']} HP is now {monster["hp"]}")

monster["Status"] = "Angry"

print(monster)