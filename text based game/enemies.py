import time
import main
import Player
import random
import Sceniros

def Crayzed_Hotel_Suriver1():
    CHS_health = 50
    print ("You encounter Crayzed, a menacing figure with a wild look in his eyes. He blocks your path and growls,\n")
    time.sleep(.5)
    print ("You knowdance that they look injured, but you also know that they are dangerous.\n")
    time.sleep(1)

## If the player has a crowbar
    if "Crowbar" in main.inventory:
        print("You have a crowbar in your inventory. You can use it to defend yourself.\n")
        time.sleep(1)
        while CHS_health > 0:
            CBaction = input("Do you want to (1) Fight or (2) Run away?\n")
            if CBaction == '1':
                CBactiondamage = random.randint(5, 15) * 2  # Double damage with crowbar
                CHS_health -= CBactiondamage
                print(f"You attack Crayzed and deal {CBactiondamage} damage. Crayzed's health is now {CHS_health}.\n")
                if CHS_health <= 0:
                    print("You have defeated Crayzed!\n")
                    Sceniros.CHS_Room()
                    return True
                else:
                    enemy_damage = random.randint(5, 10)
                    print(f"Crayzed attacks you and deals {enemy_damage} damage.\n")
                    main.health -= enemy_damage
                    print(f"Your health is now {main.health}.\n")
            elif CBaction == '2':
                print("You run away from Crayzed, escaping the danger for now.\n")
                return False
            else:
                print("Invalid choice. Please choose 1 or 2.\n")

    if main.health <= 0:
        print("You have been defeated by Crayzed. Game Over.\n")
        main.gameover()
    
## If the player does not have a crowbar
    if "Crowbar" not in main.inventory:
        print("You do not have any weapons to defend yourself with. You must fight Crayzed with your bare hands.\n")
        time.sleep(1)
        while CHS_health > 0:
            action = input("Do you want to (1) Fight or (2) Run away?\n")
            if action == '1':
                damage = random.randint(5, 15) 
                CHS_health -= damage
                print(f"You attack Crayzed and deal {damage} damage. Crayzed's health is now {CHS_health}.\n")
                if CHS_health <= 0:
                    print("You have defeated Crayzed!\n")
                    Sceniros.CHS_Room()
                    return True
                else:
                    enemy_damage = random.randint(5, 10)
                    print(f"Crayzed attacks you and deals {enemy_damage} damage.\n")
                    main.health -= enemy_damage
                    print(f"Your health is now {main.health}.\n")
            elif action == '2':
                print("You run away from Crayzed, escaping the danger for now.\n")
                return False
            else:
                print("Invalid choice. Please choose 1 or 2.\n")

    if main.health <= 0:
        print("You have been defeated by Crayzed. Game Over.\n")
        main.gameover()

    
