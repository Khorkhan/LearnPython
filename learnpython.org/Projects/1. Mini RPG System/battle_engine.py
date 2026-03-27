import csv
import json
from io import StringIO

csv_data = """name,hp,exp
Slime,20,5
Goblin,50,15
Dragon,1000,500"""

f = StringIO(csv_data)
reader = csv.DictReader(f)

enemies = [row for row in reader]

def log_action(func):
    def wrapper(*args, **kwargs):
        print("Action Log: Player attack!")
        result = func(*args, **kwargs)
        return result
    return wrapper

#function attack
@log_action
def attack(enemy, damage):
    enemy["hp"] = max(int(enemy["hp"]) - damage, 0)
    print(f"{enemy['name']} now has {enemy['hp']} HP left.")
    return enemy

# JSON: Save game
def save_game(player_data):
    json_string = json.dumps(player_data)
    print("Game Saved: ", json_string)
    return json_string

# Filter: choose only monster hp > 0
def alive_monsters(monsters):
    return list(filter(lambda m: int(m["hp"]) > 0, monsters))

# lambda/map:buff player attack temporary
def buff_attack(base_atk):
    buffed = list(map(lambda atk: atk * 2, [base_atk]))
    return buffed[0]

# test system battle engine
player = {"name": "Hero", "atk": 50, "hp": 200}

#buff atk
player["atk"] = buff_attack(player["atk"])
print("Player buffed attack: ", player["atk"])

#attack 1st enemy
attack(enemies[0], player["atk"])

alive = alive_monsters(enemies)
print("Alive Monsters: ", [m["name"] for m in alive])

save_game(player)