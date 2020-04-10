# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    def __init__(self, name, year):  # This function is a base class
        pass


class GroundVehicle(Vehicle):  # This is a base class
    def __init__(self, number_of_wheels, name, year):
        self.number_of_wheels = number_of_wheels
        super().__init__(name, year)


class Car(GroundVehicle):
    def __init__self(self, brand, number_of_wheels, name, year):
        self.brand = brand
        super().__init__(number_of_wheels)


class Motorcycle(GroundVehicle):
    def __init__self(self, speed, number_of_wheels, name, year):
        self.speed = speed
        super().__init__(number_of_wheels)


class FlightVehicle(Vehicle):
    def __init__(self, name, year, model):  # This is also a base function
        self.name = name
        self.model = model
        super().__init__(year)
