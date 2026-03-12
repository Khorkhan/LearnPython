# create function (defining a function)
def say_hello():
    print("Hello from a function!")

# calling
say_hello()

# function(arguments)
def greet_user(username):
    print(f"Hello, {username}!")

greet_user("Adam")
greet_user("Alice")

def sum_numbers(a,b):
    return a + b

result = sum_numbers(5, 10)
print(result)

# exercise
# function returns list of benefits
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse"]

# receive functions to make sentence
def build_sentence(benefit):
    return f"{benefit} is a benefit of functions!"

# work with for loop
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        # call 2nd functions and print result
        print(build_sentence(benefit))

name_the_benefits_of_functions()