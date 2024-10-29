import random

class Game:
    """
    Manages the game state and user interactions.
    """
    def __init__(self, player, locations):
        self.player = player
        self.locations = {location.name.lower(): location for location in locations}
        self.current_location = self.locations[self.player.location.lower()]

    def move_to(self, location_name):
        location = self.locations.get(location_name.lower())
        if location:
            self.player.location = location.name
            self.current_location = location
            return f"You have moved to {location.name}."
        else:
            return "Location not found."

    def encounter_monster(self, monster):
        # Simple combat mechanic
        response = ""
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
        if not self.player.is_alive():
            response += "You have been slain by the monster..."
        return response

    def get_state_json(self):
        return self.player.to_dict()