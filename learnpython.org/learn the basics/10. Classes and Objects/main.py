# define class
class Vehicle:
    name = ""
    kind = "car"
    value = 100.00

    # talent class (Method)
    def description(self):
        desc_str = f"{self.name} is a {self.kind} worth ${self.value:.2f}."
        return desc_str
    
# create Object (instance)
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())

# exercise
class Phone:
    # The constructor (__init__) is used to initialize attributes.
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # method (Class talent)
    def get_info(self):
        return f"This phone is a {self.brand} {self.model}. It costs ${self.price}."
    
# create object from class
my_phone = Phone("Apple", "iPhone 15", 799)

# call method and print
print(my_phone.get_info())