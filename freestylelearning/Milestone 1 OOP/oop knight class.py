class knight:
    #Constructor
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    #Method
    def show_info(self):
        print(f"--- {self.name} ---")
        print(f"HP: {self.hp} | Atk: {self.atk}")

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.atk} damage!")
        enemy.hp -= self.atk

player = knight("Iris", 100, 25)
monster = knight("Slime", 50, 5)

player.show_info()
player.attack(monster)
print(f"Monster's HP Remaining: {monster.hp}")