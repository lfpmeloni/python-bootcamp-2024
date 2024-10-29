from inventory import Inventory

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