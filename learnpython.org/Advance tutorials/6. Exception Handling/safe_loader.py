inventory = {"Sword": 1, "Potion": 5}
try:
    print(inventory["Shield"])
except KeyError:
    print("Item not found in inventory")
finally:
    print("Item check complete.")