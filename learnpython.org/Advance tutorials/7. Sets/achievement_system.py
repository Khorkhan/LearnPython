raw_rewards = ["First Blood", "First Blood", "Boss Slayer", "First Blood", "Collector"]
unique_rewards = set(raw_rewards)
print("Unique rewards: ", unique_rewards)

all_achievements = {"First Blood", "Boss Slayer", "Collector", "Legendary Hero"}
missing_achievements = all_achievements.difference(unique_rewards)
print("Missing Achievements: ", missing_achievements)