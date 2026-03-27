def show_rewards(quest_name, *items):
    print(f"Quest: {quest_name} completed!")
    print("Rewards received: ")
    for item in items:
        print(item)

show_rewards("Dragon Slayer", "Gold x100", "Dragon Scale", "Legendary Sword")