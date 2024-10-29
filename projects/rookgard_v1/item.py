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
    
#TODO create inheritance types:
# Equipment: Helments, Armors, Legs, Boots, Schields
# Weapons: Axes, Clubs, Swords, Distance Weapons, Amulets and Necklaces, Rings
# Food: