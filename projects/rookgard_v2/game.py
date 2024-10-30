# game.py

import random
from classes import Monster, Item, Player, Inventory, Location

class Game:
    """
    Manages the game state and user interactions.
    """
    def __init__(self, player, locations):
        self.player = player
        self.locations = {location.name.lower(): location for location in locations}
        self.current_location = self.locations[self.player.location.lower()]
        self.active_monsters = []  # Monsters currently in the location

    def move_to(self, location_name):
        location = self.locations.get(location_name.lower())
        if location:
            self.player.location = location.name
            self.current_location = location
            self.active_monsters = location.monsters.copy()  # Update active monsters
            return f"You have moved to {location.name}."
        else:
            return "Location not found."

    def explore_current_location(self):
        current_loc = self.current_location
        response = f"Exploring {current_loc.name}: {current_loc.description}\n"
        self.active_monsters = current_loc.monsters.copy()  # Update active monsters
        if self.active_monsters:
            response += "You encounter the following monsters:\n"
            for idx, monster in enumerate(self.active_monsters, 1):
                response += f"{idx}. {monster.name} (Life: {monster.life})\n"
        else:
            response += "There are no monsters here.\n"

        if current_loc.items:
            response += "You found the following items:\n"
            for item in current_loc.items:
                response += f"- {item.name}: {item.description}\n"
                self.player.inventory.add_item(item)
            current_loc.items.clear()
        else:
            response += "There are no items to collect here.\n"

        return response

    def fight_monster(self, monster_index):
        if monster_index < 1 or monster_index > len(self.active_monsters):
            return "Invalid monster selection."

        monster = self.active_monsters[monster_index - 1]
        response = f"You engage in battle with {monster.name}!\n"

        while monster.is_alive() and self.player.is_alive():
            player_attack = random.randint(5, 15)
            monster.take_damage(player_attack)
            response += f"You attack {monster.name} for {player_attack} damage.\n"
            if monster.is_alive():
                monster_attack = monster.attack()
                self.player.take_damage(monster_attack)
                response += f"{monster.name} attacks you for {monster_attack} damage.\n"
            else:
                self.player.gain_experience(monster.experience)
                response += f"You have defeated {monster.name} and gained {monster.experience} experience.\n"
                # Loot drop
                if monster.loot:
                    dropped_item = random.choice(monster.loot)
                    self.player.inventory.add_item(dropped_item)
                    response += f"{monster.name} dropped {dropped_item.name}.\n"
                # Remove defeated monster from active monsters
                self.active_monsters.remove(monster)

        if not self.player.is_alive():
            response += "You have been slain by the monster..."
        return response

    def use_item(self, item_name):
        item = self.player.inventory.remove_item(item_name)
        if item:
            if item.item_type.lower() == "consumable":
                if item.name.lower() == "health potion":
                    self.player.life += 50
                    if self.player.life > 100:
                        self.player.life = 100
                    return "You used a Health Potion and restored 50 life points."
                else:
                    return f"You used {item.name}, but nothing happened."
            else:
                return f"You cannot use {item.name}."
        else:
            return f"No item named {item_name} found in inventory."

    def get_state_json(self):
        return self.player.to_dict()
