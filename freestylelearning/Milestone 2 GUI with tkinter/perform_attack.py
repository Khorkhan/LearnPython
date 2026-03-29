import tkinter as tk

class Entity:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0
    
def perform_attack():
    if hero.is_alive() and boss.is_alive():
        #Hero attack
        hero_dmg = hero.atk
        boss.hp -= hero_dmg
        if boss.hp < 0:
            boss.hp = 0

        log_label.config(text=f"{hero.name} dealt {hero_dmg} damage!")
        boss_hp_label.config(text=f"Boss HP: {boss.hp}")


        #check if boss is alive -> counter
        if boss.is_alive():
            boss_dmg = boss.atk
            hero.hp -= boss_dmg
            if hero.hp < 0:
                hero.hp = 0

            log_label.config(text=f"{hero.name} dealt {hero_dmg} damage! \n {boss.name} countered for {boss_dmg} damage!")
            hero_hp_label.config(text=f"Hero HP: {hero.hp}")

        #if boss dead
        if not boss.is_alive():
            log_label.config(text="Victory! The Throne is yours!", fg="gold", bg="black")
            attack_btn.config(state="disabled")

        #if hero dead
        if not hero.is_alive():
            log_label.config(text="you have fallen...", fg="gray")
            attack_btn.config(state="disabled")

# characters
hero = Entity("Iris", 100, 20)
boss = Entity("Dark lord", 150, 10)

#create window
root = tk.Tk()
root.title("The Holy Throne: battle")
root.geometry("800x600")

#ui elements
hero_hp_label = tk.Label(root, text=f"Hero HP: {hero.hp}", font=("arial", 14), fg="blue")
hero_hp_label.pack(pady=10)

boss_hp_label = tk.Label(root, text=f"Boss HP: {boss.hp}", font=("arial", 18, "bold"), fg="red")
boss_hp_label.pack(pady=20)

log_label = tk.Label(root, text="A Battle begins... ", font=("Arial", 10, "italic"))
log_label.pack(pady=10)

#attack button
attack_btn = tk.Button(root, text="Attack!", command=perform_attack, width=20, height=2, bg="darkred", fg="white")
attack_btn.pack(pady=20)

root.mainloop()