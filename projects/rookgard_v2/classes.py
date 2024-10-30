# classes.py

import random

class Item:
    """
    Represents an item in the game.
    """
    def __init__(self, name, description, value, item_type):
        self.name = name
        self.description = description
        self.value = value
        self.item_type = item_type

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "value": self.value,
            "type": self.item_type
        }

class Monster:
    """
    Represents a monster in the game.
    """
    def __init__(self, name, life, attack_power, loot, experience):
        self.name = name
        self.life = life
        self.attack_power = attack_power
        self.loot = loot  # List of Item objects
        self.experience = experience

    def is_alive(self):
        return self.life > 0

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.life -= damage

    def to_dict(self):
        return {
            "name": self.name,
            "life": self.life,
            "attack_power": self.attack_power,
            "experience": self.experience
        }

class Player:
    """
    Represents the player.
    """
    def __init__(self, name):
        self.name = name
        self.life = 100
        self.experience = 0
        self.level = 1
        self.inventory = Inventory()
        self.location = "Starting Point"

    def is_alive(self):
        return self.life > 0

    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        required_exp = self.level * 100
        if self.experience >= required_exp:
            self.level += 1
            self.experience -= required_exp
            self.life += 20  # Increase life on level up

    def take_damage(self, damage):
        self.life -= damage

    def to_dict(self):
        return {
            "name": self.name,
            "life": self.life,
            "experience": self.experience,
            "level": self.level,
            "inventory": self.inventory.to_list(),
            "location": self.location
        }

class Inventory:
    """
    Manages the player's inventory.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None

    def to_list(self):
        return [item.to_dict() for item in self.items]

class Location:
    """
    Represents a location in the game world.
    """
    def __init__(self, name, description, monsters, items):
        self.name = name
        self.description = description
        self.monsters = monsters  # List of Monster objects
        self.items = items  # List of Item objects

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "monsters": [monster.to_dict() for monster in self.monsters],
            "items": [item.to_dict() for item in self.items]
        }
