class Entity:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0
    
    def attack(self, other):
        print(f"{self.name} attacks {other.name} for {self.atk} damage!")
        other.hp -= self.atk
        if other.hp < 0:
            other.hp = 0
        print(f"{other.name}'s HP is now {other.hp}")

hero = Entity("Hero", 100, 20)
boss = Entity("Boss", 120, 15)

# Fighting loop
while hero.is_alive and boss.is_alive():
    hero.attack(boss)
    if not boss.is_alive():
        print(f"{boss.name} has fallen {hero.name} wins!")
        break

    boss.attack(hero)
    if not hero.is_alive():
        print(f"{hero.name} has fallen! {boss.name} wins!")
        break