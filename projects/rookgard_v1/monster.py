import random

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