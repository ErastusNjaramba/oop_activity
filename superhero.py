# Base Superhero class
class Superhero:
    def __init__(self, name, power_level, secret_identity):
        self._name = name  # Protected attribute for encapsulation
        self._power_level = power_level
        self._secret_identity = secret_identity
        self._is_active = True

    # Method to get hero status
    def get_status(self):
        return f"{self._name} is {'active' if self._is_active else 'retired'} with power level {self._power_level}"

    # Method to retire hero
    def retire(self):
        self._is_active = False
        return f"{self._name} has retired!"

    # Getter for name (encapsulation)
    @property
    def name(self):
        return self._name

# Flying Superhero subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level, secret_identity, flight_speed):
        super().__init__(name, power_level, secret_identity)
        self.flight_speed = flight_speed

    # Flying-specific method
    def soar(self):
        return f"{self._name} soars at {self.flight_speed} mph!"

# Main program to demonstrate the classes
def main():
    # Create superheroes
    superman = FlyingSuperhero("Superman", 95, "Clark Kent", 1000)
    batman = Superhero("Batman", 70, "Bruce Wayne")

    # Demonstrate methods
    print("Superhero Demo:")
    print(superman.get_status())
    print(superman.soar())
    print(batman.get_status())
    print(batman.retire())
    print(batman.get_status())

if __name__ == "__main__":
    main()