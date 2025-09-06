import Player
import time
import MainMenu
import random
import main

def starting_point():
    """The first scenario of the game."""
    print("\nYou wake up in a dimly lit room. You don't remember how you got here.")
    
    while True:
        choice = input(f"What will you do?\n 1.Check your inventory.\n 2.Search the room.\n 3.Rest for a while.\n 4.Try and leave room.\n 5.Scream for help.\n 6.Show stats.\n")
        if choice == '1':
            time.sleep(1)
            Player.show_inventory(main.inventory)
        elif choice == '2':
            print("\nYou fumble around the room but find nothing of interest.\n")
            time.sleep(1)
        elif choice == '3':
            print("\nYou try to rest but the uneasiness of the room keeps you awake.\n")
            time.sleep(1)
        elif choice == '4':
            print("\nYou try the door handle, when you open the door it lets out a sharp creaking sound.\n")
            time.sleep(1)
            print("You step out into the hallway.\n")
            return hallway()
        elif choice == '5':
            print("\nYou scream for help, but your voice echoes back to you.\n")
            time.sleep(1)
        elif choice == '6':
            time.sleep(1)
            Player.show_stats(main.name, main.Strength, main.Intelligence, main.Agility, main.Vision)
        else:
            print("Invalid choice. Please choose a valid option.\n")

def hallway():
    print("You are in a long, dark hallway. There are doors on either side of you.\n")

    while True:
        choice = input(f"What will you do?\n 1.Check your inventory.\n 2.Walk down the hallway.\n 3.Open the door to your left\n 4.Go back to the room")
        if choice == '1':
            time.sleep(1)
            Player.show_inventory(main.inventory)
        if choice == '2':
            print("\nYou walk down the hallway, past some closed doors with strange markings.\n")
            time.sleep(1)
            hallway_part2()
        if choice == '3':
            print("\nYou notice that the door is slightly ajar.\n You push it open and step inside.\n")
            time.sleep(1)
            First_room()

def First_room():
    print("You enter a small room with a table and a chair. On the table, there is a key.\n")
    while True:
        choice = input(f"What will you do?\n 1.Check your inventory.\n 2.Take the key.\n 3.Explore the room.\n 4.Go back to the hallway.\n")
        if choice == '1':
            time.sleep(1)
            Player.show_inventory(main.inventory)
        if choice == '2':
            print("\nYou take the key and put it in your inventory.\n")
            time.sleep(1)
            main.inventory = Player.add_to_inventory(main.inventory, "Key")
        if choice == '4':
            print("\nYou go back to the hallway.\n")
            return hallway()
        if choice == '3':
            print("\nYou explore the room and you find a hidden compartment under the floorboards.\n While searching the compartmant you only find a crowbar.\n")
            main.inventory = Player.add_to_inventory(main.inventory, "Crowbar")
            time.sleep(1)

        
def hallway_part2():
    print("You are in a long, dark hallway. There are doors on either side of you.\n")

if __name__ == "__main__":
    First_room()