hello = "Hello" + " " + "World"
print(hello)

lots_of_hellos = "Hello " * 5
print(lots_of_hellos)

even_numbers = [2, 4, 6]
odd_numbers = [1, 3, 5]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1, 2, 3] * 3)

#exercise
#create x * 10
x_list = ["x"] * 10

#create y * 10
y_list = ["y"] * 10

# combine
big_list = x_list + y_list

print(f"x_list: {x_list}")
print(f"y_list: {y_list}")
print(f"big_list length: {len(big_list)}")
print(f"big_list {big_list}")