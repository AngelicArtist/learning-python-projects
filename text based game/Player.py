from tkinter import Place
import random
import main
import MainMenu
import time

def show_stats(name, Strength, Intelligence, Agility, Vision):
    print(f"{name}'s stats:\n")
    print(f"Strength: {Strength}")
    print(f"Intelligence: {Intelligence}")
    print(f"Agility: {Agility}")
    print(f"Vision: {Vision}")

def show_inventory(inventory):
    if not inventory:
        print("Your inventory is empty.")
        time.sleep(.5)
    else:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")

def add_to_inventory(inventory, item):
    inventory.append(item)
    print(f"{item} has been added to your inventory.")
    return inventory

def remove_from_inventory(inventory, item):
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has been removed from your inventory.")
    else:
        print(f"{item} is not in your inventory.")
    return inventory

if __name__ == "__main__":
    print("This is the Player module.")
