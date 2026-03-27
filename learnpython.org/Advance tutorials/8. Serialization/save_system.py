import json

player_data = {
    "name": "Aris",
    "level": 25,
    "items": ["Health Potion", "Ancient Sword"]
}

json_string = json.dumps(player_data)
print("JSON String: ", json_string)

loaded_data = json.loads(json_string)

print("Loaded name: ", loaded_data["name"])