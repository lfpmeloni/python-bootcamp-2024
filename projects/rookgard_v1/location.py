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