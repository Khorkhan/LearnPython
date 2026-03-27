def mana_check(func):
    def wrapper(*args, **kwargs):
        print("Checking mana... [OK]")
        result = func(*args, **kwargs)
        return result
    return wrapper

@mana_check
def cast_fireball():
    print("Fireball Launched!")

cast_fireball()