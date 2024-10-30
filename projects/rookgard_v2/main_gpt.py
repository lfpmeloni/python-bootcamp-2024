# main_gpt.py

import json
import os
import sys
import openai
from dotenv import load_dotenv
from classes import Player
from game import Game
from game_data import initialize_items, initialize_monsters, initialize_locations

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Error: The OPENAI_API_KEY environment variable is not set.")
    print("Please set it in a .env file or your system environment variables.")
    sys.exit(1)

openai.api_key = OPENAI_API_KEY

def get_chatgpt_response(prompt):
    """
    Sends a prompt to ChatGPT and retrieves the response.

    Parameters:
        prompt (str): The prompt to send to ChatGPT.

    Returns:
        str: The assistant's response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": """
You are ChatGPT, a large language model trained by OpenAI.
You assist in a text-based RPG game by generating dynamic descriptions and events based on player actions.
You have access to the following methods to enhance the game:
- generate_monster(name, life, attack_power, loot, experience): Creates a new monster.
- create_item(name, description, value, item_type): Creates a new item.
- create_location(name, description, monsters, items): Creates a new location.
Ensure that all responses are concise (less than a paragraph) and relevant to the player's actions.
Do not include any additional text outside the scope of the game description.
"""},  # Updated system prompt for clarity
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Limit to ensure concise responses
            temperature=0.5,  # Lower temperature for more deterministic outputs
            n=1,
            stop=None
        )
        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content'].strip()
        return reply
    except Exception as e:
        print(f"Error communicating with ChatGPT: {e}")
        return None

def main():
    print("Welcome to Rookgaard Adventure!")
    player_name = input("Enter your character's name: ").strip()
    while not player_name:
        print("Character name cannot be empty. Please enter a valid name.")
        player_name = input("Enter your character's name: ").strip()
    player = Player(name=player_name)

    # Initialize game data
    items = initialize_items()
    monsters = initialize_monsters(items)
    locations = initialize_locations(items, monsters)

    game = Game(player, locations)

    print(f"\nHello, {player.name}! Your adventure begins at the {player.location}.")

    while player.is_alive():
        print("\nWhat would you like to do?")
        print("Options: move, explore, inventory, status, state, quit")
        action = input("Enter action: ").strip().lower()

        if action == "move":
            print("\nAvailable locations:")
            for loc in locations:
                print(f"- {loc.name}")
            destination = input("Enter location to move to: ").strip()
            if destination:
                result = game.move_to(destination)
                print(f"\n{result}")
            else:
                print("\nInvalid destination.")

        elif action == "explore":
            current_loc = game.current_location
            # Generate dynamic description using ChatGPT
            prompt = f"""
Player {player.name} decides to explore the {current_loc.name}.
Provide a concise (less than a paragraph) description of the exploration and any immediate events that occur.
"""
            description = get_chatgpt_response(prompt)
            if description:
                print(f"\n{description}")
                # Handle exploration logic
                exploration_result = game.explore_current_location()
                print(exploration_result)
            else:
                print("\nFailed to generate exploration description.")

        elif action == "fight":
            if not game.active_monsters:
                print("\nThere are no monsters to fight here.")
                continue
            print("\nMonsters Available to Fight:")
            for idx, monster in enumerate(game.active_monsters, 1):
                print(f"{idx}. {monster.name} (Life: {monster.life})")
            try:
                monster_choice = int(input("Enter the number of the monster you want to fight: ").strip())
                result = game.fight_monster(monster_choice)
                print(f"\n{result}")
            except ValueError:
                print("\nInvalid input. Please enter a valid monster number.")
            except Exception as e:
                print(f"\nAn error occurred: {e}")

        elif action == "inventory":
            inventory = player.inventory.to_list()
            if inventory:
                print("\nYour Inventory:")
                for item in inventory:
                    print(f"- {item['name']}: {item['description']}")
            else:
                print("\nYour inventory is empty.")

        elif action == "status":
            status = player.to_dict()
            print("\nYour Status:")
            print(f"Name: {status['name']}")
            print(f"Life: {status['life']}")
            print(f"Experience: {status['experience']}")
            print(f"Level: {status['level']}")
            print(f"Location: {status['location']}")

        elif action == "state":
            state_json = json.dumps(game.get_state_json(), indent=4)
            print("\n--- Player State ---")
            print(state_json)
            print("--------------------")

        elif action == "quit":
            print("\nThank you for playing Rookgaard Adventure!")
            break

        else:
            print("\nUnknown action. Please try again.")

    if not player.is_alive():
        print("\nGame Over.")

if __name__ == "__main__":
    main()
