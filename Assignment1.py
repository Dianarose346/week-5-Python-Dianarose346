class Superhero:
    def __init__(self, name, power, strength):
        self.name = name       # Name of the superhero
        self.power = power     # The superhero's special power
        self.strength = strength  # The superhero's strength level

    def use_power(self):
        print(f"{self.name} is using their {self.power} power!")

    def display_strength(self):
        print(f"{self.name}'s strength level is {self.strength}.")

# Inheriting from Superhero class
class FlyingHero(Superhero):
    def __init__(self, name, power, strength, flying_speed):
        super().__init__(name, power, strength)
        self.flying_speed = flying_speed  # Extra attribute for flying speed

    def fly(self):
        print(f"{self.name} is flying at {self.flying_speed} speed!")

# Creating objects of Superhero and FlyingHero
hero1 = Superhero("Wonder Woman", "Super Strength", 10)
hero1.use_power()  # Output: Wonder Woman is using their Super Strength power!

hero2 = FlyingHero("Superman", "Flight", 15, 500)
hero2.fly()  # Output: Superman is flying at 500 speed!
hero2.use_power()  # Output: Superman is using their Flight power!
hero2.display_strength()  # Output: Superman's strength level is 15.
