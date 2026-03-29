import tkinter as tk

#Entity Class
class Entity:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, other):
        other.hp -= self.atk
        if other.hp < 0:
            other.hp = 0

#battle logic
def perform_attack():
    if hero.is_alive() and boss.is_alive():
        #hero attack
        hero.attack(boss)
        log_label.config(text=f"{hero.name} dealt {hero.atk} damage!")
        boss_hp_label.config(text=f"Boss HP: {boss.hp}")

        #if boss still alive
        if boss.is_alive():
            boss.attack(hero)
            log_label.config(text=f"{hero.name} dealt {hero.atk} damage! \n {boss.name} countered for {boss.atk} damage!")
            hero_hp_label.config(text=f"Hero HP: {hero.hp}")

        #condition boss to die
        if not boss.is_alive():
            log_label.config(text="The holy Throne has been reclaimed!", fg="gold", bg="black")
            attack_btn.config(state="disabled")

        #condition hero to die
        if not hero.is_alive():
            log_label.config(text="You have fallen...", fg="gray")
            attack_btn.config(state="disabled")

# travel logic
current_location = "The Inn"

world_map = {
    "The Inn": "You are in the cozy Inn",
    "The Road": "You are walking on the road",
    "The Cathedral": "You are standing in front of the Cathedral"
}

def move():
    global current_location
    if current_location == "The Inn":
        current_location = "The Road"
    elif current_location == "The Road":
        current_location = "The Cathedral"

    #update location
    loc_label.config(text=f"Location: {current_location}")
    desc_label.config(text=world_map[current_location])

    #when at the cathedral change to start battle
    if current_location == "The Cathedral":
        move_btn.config(text="Start Battle!", bg="gold", fg="black", command=start_battle)

def start_battle():
    # hide travel btn
    move_btn.pack_forget()
    desc_label.pack_forget()
    loc_label.pack_forget()

    #show ui battle
    hero_hp_label.pack(pady=10)
    boss_hp_label.pack(pady=20)
    log_label.pack(pady=10)
    attack_btn.pack(pady=20)

#characters
hero = Entity("Iris", 100, 20)
boss = Entity("Dark lord", 150, 15)

#gui setup
root = tk.Tk()
root.title("The Holy Throne")
root.geometry("800x600")

#travel ui
loc_label = tk.Label(root, text=f"Location: {current_location}", font=("Arial", 16, "bold"))
loc_label.pack(pady=10)

desc_label = tk.Label(root, text=world_map[current_location], font=("Arial, 12"))
desc_label.pack(pady=20)

move_btn = tk.Button(root, text="Move Forward", command=move, width=20, height=2)
move_btn.pack(pady=20)

#battle ui
hero_hp_label = tk.Label(root, text=f"Hero HP: {hero.hp}", font=("Arial", 14), fg="blue")
boss_hp_label = tk.Label(root, text=f"Boss: {boss.hp}", font=("Arial", 18, "bold"), fg="red")
log_label = tk.Label(root, text="A battle begins... ", font=("Arial", 10, "italic"))
attack_btn = tk.Button(root, text="Attack!", command=perform_attack, width=20, height=2, bg="darkred", fg="white")

root.mainloop()