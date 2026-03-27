def enemy_generator():
    yield "Slime"
    yield "Goblin"
    yield "Orc"

gen = enemy_generator()

print(next(gen))

for enemy in gen:
    print(enemy)

def enemy_index_generator():
    for i in range(10):
        yield i

for idx in enemy_index_generator():
    print(f"Enemy #{idx}")