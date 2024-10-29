# main.py

import json
from player import Player
from game import Game
from game_data import initialize_items, initialize_monsters, initialize_locations

def main():
    print("Welcome to Rookgaard Adventure!")
    player_name = input("Enter your character's name: ")
    player = Player(name=player_name)
    
    # Initialize game data
    items = initialize_items()
    monsters = initialize_monsters(items)
    locations = initialize_locations(items, monsters)
    
    game = Game(player, locations)
    
    print(f"Hello, {player.name}! Your adventure begins at the {player.location}.")
    
    while player.is_alive():
        print("\nWhat would you like to do?")
        print("Options: move, explore, inventory, status, quit")
        action = input("Enter action: ").strip().lower()
        
        if action == "move":
            print("Available locations:")
            for loc in locations:
                print(f"- {loc.name}")
            dest = input("Enter location to move to: ").strip()
            result = game.move_to(dest)
            print(result)
        
        elif action == "explore":
            current_loc = game.current_location
            print(f"Exploring {current_loc.name}: {current_loc.description}")
            if current_loc.monsters:
                print("You encounter the following monsters:")
                for idx, monster in enumerate(current_loc.monsters, 1):
                    print(f"{idx}. {monster.name} (Life: {monster.life})")
                choice = input("Choose a monster to fight or type 'run': ").strip().lower()
                if choice == "run":
                    print("You decide to flee.")
                else:
                    try:
                        monster_idx = int(choice) - 1
                        if 0 <= monster_idx < len(current_loc.monsters):
                            monster = current_loc.monsters[monster_idx]
                            battle_result = game.encounter_monster(monster)
                            print(battle_result)
                            if not monster.is_alive():
                                current_loc.monsters.remove(monster)
                        else:
                            print("Invalid monster selection.")
                    except ValueError:
                        print("Invalid input.")
            else:
                print("There are no monsters here.")
        
        elif action == "inventory":
            inventory = player.inventory.to_list()
            if inventory:
                print("Your Inventory:")
                for item in inventory:
                    print(f"- {item['name']}: {item['description']}")
            else:
                print("Your inventory is empty.")
        
        elif action == "status":
            status = player.to_dict()
            print("Your Status:")
            print(f"Name: {status['name']}")
            print(f"Life: {status['life']}")
            print(f"Experience: {status['experience']}")
            print(f"Level: {status['level']}")
            print(f"Location: {status['location']}")
        
        elif action == "quit":
            print("Thank you for playing Rookgaard Adventure!")
            break
        
        else:
            print("Unknown action. Please try again.")
        
        # After action, return JSON state
        state_json = json.dumps(game.get_state_json(), indent=4)
        
        if not player.is_alive():
            print("Game Over.")
            break

if __name__ == "__main__":
    main()
