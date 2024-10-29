"""
class_day_13.py
Author: Felipe Meloni  
Date: 2024-10-29
Description: Classes
"""

import random

# Example of a class

class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    # Magic methods
    def __str__(self) -> str:
        return f"{self.name},{self.age}. A {self.breed} with the color {self.color}"
    
    def eat(self, food):
        if not type(food) == str:
            raise TypeError('Food has to be a string!')
        return f"{self.name} is eating {food}."

dog1 = Dog('Frada','Stray',3,'Red Caramel')

print(dog1)
print(dog1.breed)
print(dog1.eat('banana'))

# My own class

class Creature:
    """
    Represents a creature in the game.
    """
    def __init__(self, name, experience, life, attack_power, loot):
        self.name = name
        self.experience = experience
        self.life = life
        self.attack_power = attack_power
        self.loot = loot  # List of Item objects

    def is_alive(self):
        return self.life > 0
    
    def attack(self):
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        self.life -= damage

chicken = Creature('Chicken', 0, 15, 0, {2, 'meat'})
print(chicken)
print(chicken.loot)

# Book Example: Restaurants

class Restaurant:
    def __init__(self, restaurant_name, cousine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = number_served

    def __str__(self):
        return f"{self.restaurant_name} is a {self.cousine_type} restaurant that has served {self.number_served} customers."
    
    def open_restaurant(self):
        return f"{self.restaurant_name} is open."
    
    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
        return f"{self.restaurant_name} has served {self.number_served} customers."
    
    def increment_number_served(self, served_customers):
        self.number_served += served_customers
        return f"{self.restaurant_name} has served {served_customers} new customers today to a total of {self.number_served} customers."
    
restaurant1 = Restaurant("Giordano", "Italian")
restaurant2 = Restaurant("Mey Izakaya", "Japanese")
restaurant3 = Restaurant("Adler Platz", "German")

# print(restaurant1.describe_restaurant()) -> changed the describe_restaurant() function for __str__
print(restaurant1)
print(restaurant2.open_restaurant())
print(restaurant3.set_number_served(23))
print(restaurant3.increment_number_served(5))

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)  # Call the parent class's constructor
        self.flavors = flavors  # Initialize flavors attribute

    def display_flavors(self):
        return f"Available ice cream flavors at {self.restaurant_name}: {', '.join(self.flavors)}"
    
ice_cream_stand = IceCreamStand(
    restaurant_name="Sweet Treats",
    cuisine_type="Ice Cream",
    flavors=["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]
)

print(ice_cream_stand.display_flavors())  