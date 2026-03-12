# f-string
name = "Adam"
age = 29

# use f-string
message = f"hello, my name is {name} and I'm {age} years old"
print(message)

# format()
print("Hello, {}! You are {} years old.".format(name, age))

# Managing numbers
pi = 3.14159265
print(f" pi with 2 decimal point: {pi:.2f}")

# exercise
data = ["Atom", "Bob", 55.44]

message_data = f"Hello {data[0]}{data[1]}. Your current balance is ${data[2]}."
print(message_data)