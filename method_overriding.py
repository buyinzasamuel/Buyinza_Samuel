class Vehicle:
    def start_engine(self):
        return "Starting the engine of the vehicle."

class Car(Vehicle):
    def start_engine(self):
        return "Starting the car's engine with a key."

class Bike(Vehicle):
    def start_engine(self):
        return "Starting the bike's engine with a button."

# Usage
vehicle = Vehicle()
car = Car()
bike = Bike()

print(vehicle.start_engine())  # Output: Starting the engine of the vehicle.
print(car.start_engine())       # Output: Starting the car's engine with a key.
print(bike.start_engine())      # Output: Starting the bike's engine with a button.
