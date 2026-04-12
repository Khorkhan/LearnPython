import tkinter as tk
import random

class Entity:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0
    
# game class
class Game:
    def __init__(self):
        #hero hp random 80 - 120
        self.hero = Entity("Iris", random.randint(80, 120), 20)
        self.boss = Entity("Dark Lord", 150, 15)
        self.inventory = ["Heal Potion"]
        self.gold = 0

    def check_victory(self):
        if not self.hero.is_alive() and not self.boss.is_alive():
            return "Draw"
        elif not self.hero.is_alive():
            return "Lose"
        elif not self.boss.is_alive():
            return "Win"
        return "Playing"
    
#Travel Logic
current_location = "The Inn"

world_map = {
    "The Inn": "You are in the cozy Inn",
    "The Road": "You're walking on the road",
    "The Cathedral": "You are standing in front of The Cathedral"
}

def move():
    global current_location
    if current_location == "The Inn":
        current_location = "The Road"
    elif current_location == "The Road":
        current_location = "The Cathedral"

    # update location
    loc_label.config(text=f"Location: {current_location}")
    desc_label.config(text=world_map[current_location])

    # gold system : every walk get 5 gold
    game.gold += 5
    print("You found 5 gold!")
    gold_label.config(text=f"Gold: {game.gold}")

    # when arrive to Cathedral change btn to start battle
    if current_location == "The Cathedral":
        move_btn.config(text="Start Battle!", bg="gold", fg="black", command=start_battle)

def start_battle():
    # hide travel btn
    move_btn.pack_forget()
    desc_label.pack_forget()
    loc_label.pack_forget()

    #show battle UI
    hero_hp_label.pack(pady=10)
    boss_hp_label.pack(pady=20)
    log_label.pack(pady=10)
    attack_btn.pack(pady=20)

def perform_attack():
    if game.hero.is_alive() and game.boss.is_alive():
        # hero attack
        game.boss.hp -= game.hero.atk
        if game.boss.hp < 0:
            game.boss.hp = 0

        boss_hp_label.config(text=f"Boss HP: {game.boss.hp}")
        log_label.config(text=f"{game.hero.name} dealt {game.hero.atk} damage!")

        # boss will counter if not dead
        if game.boss.is_alive():
            game.hero.hp -= game.boss.atk
            if game.hero.hp < 0:
                game.hero.hp = 0

            hero_hp_label.config(text=f"Hero HP: {game.hero.hp}")
            log_label.config(text=f"{game.hero.name} dealt {game.hero.atk} damage!\n{game.boss.name} countered for {game.boss.atk} damage!")

        # check result
        result = game.check_victory()
        if result == "Win":
            log_label.config(text="The Holy Throne has been reclaimed!", fg="gold", bg="black")
            attack_btn.config(state="disabled")
        elif result == "Lose":
            log_label.config(text="You have fallen... ", fg="gray")
            attack_btn.config(state="disabled")

#characters
game = Game()

# GUI Setup
root = tk.Tk()
root.title("The game")
root.geometry("800x600")

# travel UI
loc_label = tk.Label(root, text=f"Location: {current_location}", font=("Arial", 16, "bold"))
loc_label.pack(pady=10)

desc_label = tk.Label(root, text=world_map[current_location], font=("Arial", 12))
desc_label.pack(pady=20)

move_btn = tk.Button(root, text="Move Forward", command=move, width=20, height=2)
move_btn.pack(pady=20)

gold_label = tk.Label(root, text=f"Gold: {game.gold}", font=("Arial", 12), fg="orange")
gold_label.pack(pady=10)

#battle Ui
hero_hp_label = tk.Label(root, text=f"Hero HP: {game.hero.hp}", font=("Arial", 12), fg="blue")
boss_hp_label = tk.Label(root, text=f"Boss HP: {game.boss.hp}", font=("Arial", 16, "bold"), fg="red")
log_label = tk.Label(root, text="A battle begins...", font=("Arial", 10, "italic"))
attack_btn = tk.Button(root, text="Attack!", command=perform_attack, width=20, height=2, bg="darkred", fg="white")

root.mainloop()