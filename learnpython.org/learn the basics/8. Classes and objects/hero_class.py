class Hero:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def introduction(self):
        print(f"I'm {self.name}, the {self.job}!")

my_hero = Hero("Aris", "Mage")
my_hero.introduction()