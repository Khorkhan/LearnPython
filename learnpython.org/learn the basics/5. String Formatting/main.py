player_name = "Atom"
gold_reward = 500
item_reward = "Magic Wand"

print(f"Congratulation, {player_name}! you received {gold_reward} gold and a {item_reward}.")

tax = 0.1
final_gold = gold_reward * (1 - tax)

print(f"After tax deduction, You received {final_gold:.2f} gold.")