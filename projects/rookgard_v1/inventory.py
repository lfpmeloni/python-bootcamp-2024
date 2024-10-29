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