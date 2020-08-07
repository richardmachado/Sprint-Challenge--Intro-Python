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

#Base class - Vehicle

class Vehicle:
    def __init__(self):
        pass

#children

class FlightVehicle(Vehicle):
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    def __init__(self):
        pass

#Grandchildren Branch of - FlightVehicle

class Starship(FlightVehicle):
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass

# Grandchildren Branch of - GroundVehicle

class Car(GroundVehicle):
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass         