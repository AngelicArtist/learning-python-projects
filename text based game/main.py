import Player
import time
import MainMenu
import random
import Sceniros

name = input("Enter your character's name: ")
inventory = []
Strength = random.randint(1, 10)
Intelligence = random.randint(1, 10)
Agility = random.randint(1, 10)
Vision = random.randint(1, 10)

if __name__ == "__main__":
    MainMenu.Start_screen()

    Sceniros.starting_point()
