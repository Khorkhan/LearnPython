x = 10
if x > 5:
    print("x is greater than 5")

score = 75

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Try again!")

#boolean operators
name = "Adam"
age = 25
if name == "Adam" and age > 20:
    print("Welcome, Adam!")

# in
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, we have apple!")

# exercise
number = 15

# check condition in order
if number > 10 and number % 2 == 0:
    print("Big Even number")
elif number > 10 and number % 2 != 0:
    print("Big Odd number")
else:
    print("Small Number")