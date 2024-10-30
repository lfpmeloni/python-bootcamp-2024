# main.py

import json
import os
import openai
from player import Player
from game import Game
from game_data import initialize_items, initialize_monsters, initialize_locations
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatgpt_response(game_state):
    """
    Sends the current game state to ChatGPT and retrieves the response.

    Parameters:
        game_state (dict): The current state of the game.

    Returns:
        dict: The parsed JSON response from ChatGPT.
    """
    prompt = f"""
    You are an AI Dungeon Master for the text-based RPG game "Rookgaard Adventure". Based on the following game state, provide the next action in a JSON format adhering to the schema below.

    ### Game State:
    {json.dumps(game_state, indent=4)}

    ### JSON Schema:
    {{
        "action": "move/explore/fight/use/inventory/status/quit",
        "details": {{
            // Additional details based on the action
            // For example, if action is "move", include "destination"
            // If action is "fight", include "monster_id"
        }},
        "message": "Short descriptive text about the outcome or next steps."
    }}

    ### Instructions:
    - The "action" field should specify the player's intended action.
    - The "details" field should contain any necessary information related to the action.
    - The "message" field should provide a brief narrative of what happens next.
    - Ensure the JSON is well-formatted and adheres to the schema.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7,
            n=1,
            stop=None
        )
        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content'].strip()
        # Attempt to parse JSON from the reply
        start = reply.find("{")
        end = reply.rfind("}") + 1
        json_str = reply[start:end]
        action_response = json.loads(json_str)
        return action_response
    except Exception as e:
        print(f"Error communicating with ChatGPT: {e}")
        return None

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
        # Prepare the current game state
        game_state = game.get_state_json()

        # Get ChatGPT's action response
        action_response = get_chatgpt_response(game_state)

        if not action_response:
            print("Failed to retrieve action from ChatGPT. Exiting game.")
            break

        # Display the message from ChatGPT
        print(f"\n{action_response.get('message', '')}")

        action = action_response.get('action')
        details = action_response.get('details', {})

        if action == "move":
            destination = details.get("destination")
            if destination:
                result = game.move_to(destination)
                print(result)
            else:
                print("No destination provided for move action.")

        elif action == "explore":
            result = game.explore_current_location()
            print(result)

        elif action == "fight":
            monster_id = details.get("monster_id")
            if monster_id is not None:
                current_loc = game.current_location
                if 0 <= monster_id < len(current_loc.monsters):
                    monster = current_loc.monsters[monster_id]
                    battle_result = game.encounter_monster(monster)
                    print(battle_result)
                    if not monster.is_alive():
                        current_loc.monsters.remove(monster)
                else:
                    print("Invalid monster ID.")
            else:
                print("No monster ID provided for fight action.")

        elif action == "use":
            item_name = details.get("item_name")
            if item_name:
                result = game.use_item(item_name)
                print(result)
            else:
                print("No item name provided for use action.")

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
            print("Unknown action received from ChatGPT.")

        # After action, return JSON state
        state_json = json.dumps(game.get_state_json(), indent=4)
        print("\n--- Player State ---")
        print(state_json)
        print("--------------------")

        if not player.is_alive():
            print("Game Over.")
            break

if __name__ == "__main__":
    main()
