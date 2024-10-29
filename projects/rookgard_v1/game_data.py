# game_data.py

from item import Item
from monster import Monster
from location import Location

def initialize_items():
    sword = Item(name="Sword", description="A sharp blade to vanquish foes.", value=150, item_type="Weapon")
    potion = Item(name="Health Potion", description="Restores 50 life points.", value=50, item_type="Consumable")
    shield = Item(name="Shield", description="Provides protection against attacks.", value=100, item_type="Armor")
    return [sword, potion, shield]

def initialize_monsters(items):
    goblin = Monster(
        name="Goblin",
        life=30,
        attack_power=10,
        loot=[items[1]],  # Health Potion
        experience=50
    )
    orc = Monster(
        name="Orc",
        life=50,
        attack_power=15,
        loot=[items[0], items[1]],  # Sword and Health Potion
        experience=100
    )
    return [goblin, orc]

def initialize_locations(items, monsters):
    starting_point = Location(
        name="Starting Point",
        description="You are at the shores of Rookgaard. Paths lead to the forest and the caves.",
        monsters=[],
        items=[items[2]]  # Shield
    )
    forest = Location(
        name="Forest",
        description="A dense forest with towering trees and hidden dangers.",
        monsters=[monsters[0]],  # Goblin
        items=[]
    )
    caves = Location(
        name="Caves",
        description="Dark and damp caves that echo with mysterious sounds.",
        monsters=[monsters[1]],  # Orc
        items=[]
    )
    return [starting_point, forest, caves]