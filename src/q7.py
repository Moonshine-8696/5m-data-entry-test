class Car:
def __init__(self, make, model,year):
    self.make = make
    self.model = model
    self.year = year
    car1 = Car("Toyota","Corolla",2020)
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def describe_car(self):
        print("")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
