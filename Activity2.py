class Vehicle:
    def move(self):
        pass  # Placeholder for the move method

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Creating objects of Car and Plane
car = Car()
plane = Plane()

# Calling the same move method for different objects
car.move()  # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
