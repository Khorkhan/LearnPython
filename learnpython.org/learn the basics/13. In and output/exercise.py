food_name = input("Please enter your favorite food: ")
food_price = input("Please enter the price: ")

# turn price into float
food_price = float(food_price)

# write data file
with open ("my_menu.txt", "w", encoding="utf-8") as file:
    file.write(f"Food: {food_name}, price: {food_price:.2f} bath.")
    print("\n--- Data Saved ---")

with open("my_menu.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Data in file is: ")
    print(content)