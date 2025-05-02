# Base Vehicle class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to be overridden for polymorphism
    def move(self):
        return f"The {self.brand} {self.model} is moving"

# Car subclass
class Car(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} is driving on the road 🚗"

# Plane subclass
class Plane(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} is flying in the sky ✈️"

# Boat subclass
class Boat(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} is sailing on the water ⛵"

# Main program to demonstrate polymorphism
def main():
    # Create different vehicles
    car = Car("Toyota", "Camry")
    plane = Plane("Boeing", "747")
    boat = Boat("Yamaha", "WaveRunner")

    # List of vehicles for polymorphic demonstration
    vehicles = [car, plane, boat]

    # Demonstrate polymorphism with move()
    print("Vehicle Movement Demo:")
    for vehicle in vehicles:
        print(vehicle.move())

if __name__ == "__main__":
    main()