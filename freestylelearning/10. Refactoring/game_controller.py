class Entity:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def is_alive(self):
        return self.hp > 0

class Game:
    def __init__(self):
        #contain character info
        self.hero = Entity("Iris", 100, 20)
        self.boss = Entity("Dark lord", 150, 15)
        self.inventory = ["Heal Potion"]

    def check_victory(self):
        if not self.hero.is_alive and not self.boss.is_alive():
            return "Draw"
        elif not self.hero.is_alive():
            return "Lose"
        elif not self.boss.is_alive():
            return "Win"
        return "Playing"
    
game = Game()

print(game.check_victory())

game.boss.hp = 0
print(game.check_victory())

game.hero.hp = 0
print(game.check_victory())