import tkinter as tk

class Entity:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0
    
def perform_attack():
    # battle logic
    if hero.is_alive() and boss.is_alive():
        hero_dmg = hero.atk
        boss.hp -= hero_dmg
        if boss.hp < 0:
            boss.hp = 0

    #update console massage
    log_label.config(text=f"Hero dealt {hero_dmg} damage!")
    boss_hp_label.config(text=f"Boss HP: {boss.hp}")

    #check boss status
    if not boss.is_alive():
        log_label.config(text="Victory! the throne is yours!", fg="gold", bg="black")

#characters
hero = Entity("Iris", 100, 20)
boss = Entity("Dark lord", 150, 10)

#created window
root = tk.Tk()
root.title("The Holy Throne: Battle")
root.geometry("800x600")

# ui elements
hero_label = tk.Label(root, text=f"{hero.name} (HP: {hero.hp})", font=("Arial", 12))
hero_label.pack(pady=10)

boss_hp_label = tk.Label(root, text=f"Boss HP: {boss.hp}", font=("Arial", 16, "bold"), fg="red")
boss_hp_label.pack(pady=20)

log_label = tk.Label(root, text="A Battle Begins...", font=("Arial", 10, "italic"))
log_label.pack(pady=10)

# attack buttons
attack_btn = tk.Button(root, text="Attack!", command=perform_attack, width=20, height=2, bg="darkred", fg="white")
attack_btn.pack(pady=20)

root.mainloop()