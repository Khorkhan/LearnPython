# create dictionary user
user_profile = {
    "name": "Adam",
    "age": 25,
    "city": "Bangkok"
}

print(user_profile)

# user index
print(user_profile["name"])
print(user_profile["age"])

# add or edit data
user_profile["job"] = "Developer"
user_profile["age"] = 27
print(user_profile)

# removing
del user_profile["city"]
# or
user_profile.pop("age")
print(user_profile)

# loop in dictionary
phonebook = {"John": 9876543210, "Jack": 789456123}

for name, number in phonebook.items():
    print(f"Phone number of {name} is {number}")

# exercise
invnetory = {
    "apple": 10,
    "banana": 20
}

# add new product
invnetory["orange"] = 15

# edit amount product
invnetory["apple"] = 5

# delete product from list
del invnetory["banana"]

print(invnetory)