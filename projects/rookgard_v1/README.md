# Rookgaard Adventure

Welcome to Rookgaard Adventure, a text-based RPG game inspired by the classic MMORPG Tibia. Explore the serene island of Rookgaard, battle formidable monsters, collect valuable loot, and embark on an exciting adventure—all through the power of your imagination and console inputs!

## Overview

Rookgaard Adventure is a minimalist text-based RPG that immerses players in the rich environment of Rookgaard. Players can explore various locations, engage in battles with monsters, collect items, gain experience, and level up—all through simple text commands in the console. The game leverages object-oriented programming principles in Python to ensure a scalable and maintainable codebase.

## Features

Exploration: Navigate through different locations such as forests, caves, and beaches.
Combat System: Encounter and battle a variety of monsters to gain experience and loot.
Inventory Management: Collect, view, and manage items you find during your adventure.
Progression: Gain experience points and level up to enhance your character's abilities.
Dynamic Interactions: Simple yet engaging text-based interactions driven by user input.
JSON State Output: After each action, the game provides a JSON representation of the player's current state.

## Getting Started

### Prerequisites

Python 3.7+: Ensure you have Python installed on your machine. You can download it from python.org.

### Installation

Clone the Repository

    git clone https://github.com/yourusername/rookgaard-adventure.git
    cd rookgaard-adventure

(Optional) Create a Virtual Environment

It's good practice to use a virtual environment to manage dependencies.

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

This project uses only standard Python libraries, so no additional installations are required.

## How to Play

Run the Game

- Navigate to the project directory and execute the main script:

    python main.py

Create Your Character

- Enter your character's name when prompted.

Choose Your Actions

- Move: Travel to different locations.
- Explore: Investigate your current location for monsters and items.
- Inventory: View the items you have collected.
- Status: Check your character's current stats.
- Quit: Exit the game.

Engage in Combat

- When you encounter monsters, choose to fight or flee.
- Defeating monsters grants experience and loot.

Progress and Level Up

- Gain experience to level up, increasing your life and abilities.

JSON State Output

After each action, view your current game state in JSON format for a structured overview of your progress.

## Project Structure

rookgaard-adventure/
│
├── classes.py          # Contains all class definitions
├── game_data.py        # Initializes game data (items, monsters, locations)
├── main.py             # Main game loop and user interaction
├── README.md           # This documentation file
└── requirements.txt    # (Optional) Lists dependencies

## Classes and Modules

classes.py
Defines the core classes used in the game:

Item: Represents items that can be collected or used.
Monster: Represents adversaries with attributes like life and attack power.
Player: Represents the player's character, tracking stats and inventory.
Inventory: Manages the collection of items the player holds.
Location: Represents different areas in Rookgaard.
Game: Manages the game state, including movement and combat.

game_data.py
Initializes the game's data:

initialize_items(): Creates and returns a list of item instances.
initialize_monsters(items): Creates and returns a list of monster instances, assigning loot from the provided items.
initialize_locations(items, monsters): Creates and returns a list of location instances, populating them with monsters and items.

main.py
Handles the game loop and user interactions:

Prompts the player for actions.
Processes movement, exploration, combat, and inventory management.
Displays the player's current state in JSON format after each action.

## Game Flow

Start Game

- Player enters their character's name.
Game initializes with default stats and starting location.

Choose Actions

- Move: Select a new location to travel to.
- Explore: Investigate the current location, potentially encountering monsters or finding items.
- Inventory: View collected items.
- Status: View current stats (life, experience, level, location).
- Quit: Exit the game.

Combat

Upon encountering a monster, choose to fight or flee.

If fighting:

- Turn-based combat where both player and monster attack until one is defeated.
- If the player wins, gain experience and possibly loot.
- If the player loses, the game ends.

Progression

- Gain experience to level up.
- Leveling up increases life and other potential stats.

Game State

- After each action, the game outputs the player's current state in JSON format, detailing inventory, life, experience, level, and location.

JSON Output

After each action, the game provides a JSON representation of the player's current state. This includes:

Name: Player's character name.
Life: Current life points.
Experience: Accumulated experience points.
Level: Current level.
Inventory: List of items held, each with name, description, value, and type.
Location: Current location in the game world.
Example

    {
        "name": "Arthas",
        "life": 80,
        "experience": 150,
        "level": 2,
        "inventory": [
            {
                "name": "Health Potion",
                "description": "Restores 50 life points.",
                "value": 50,
                "type": "Consumable"
            },
            {
                "name": "Sword",
                "description": "A sharp blade to vanquish foes.",
                "value": 150,
                "type": "Weapon"
            }
        ],
        "location": "Forest"
    }

## Future Enhancements

While the current MVP provides a foundational text-based RPG experience, several features can be added to enhance gameplay:

ChatGPT Integration: Utilize ChatGPT's API to generate dynamic descriptions and interactions.
Item Usage: Implement functionality to use or equip items from the inventory.
Additional Content: Add more locations, monsters, and items to enrich the game world.
Quests and Objectives: Introduce quests to guide the player's adventure.
Save and Load: Allow players to save their progress and load it later.
Enhanced Combat Mechanics: Introduce skills, abilities, and more strategic combat options.

## Contributing

Contributions are welcome! If you'd like to enhance the game or fix bugs, please follow these steps:

Fork the Repository

Create a New Branch

    git checkout -b feature/YourFeatureName

Commit Your Changes

    git commit -m "Add some feature"

Push to the Branch

    git push origin feature/YourFeatureName

Open a Pull Request

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

## License

This project is licensed under the MIT License.

## Acknowledgments

Inspired by the classic MMORPG Tibia and its starting island Rookgaard.
