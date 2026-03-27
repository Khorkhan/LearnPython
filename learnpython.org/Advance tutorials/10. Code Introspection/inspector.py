class Weapon:
    def __init__(self):
        self.damage = 50

    def slash(self):
        pass

sword = Weapon()

print("dir(sword): ")
print(dir(sword))

print("Has durability?: ", hasattr(sword, "durability"))
print("Type of sword: ", type(sword))