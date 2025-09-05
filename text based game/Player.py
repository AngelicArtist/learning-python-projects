from tkinter import Place
import random

def create_character():
    name = input("Enter your character's name: ")

    ##Stats
    Strangth = random.randint(1,10)
    print(f"{name}, your strangth stat : {Strangth}")

    Intelligence = random.randint(1,10)
    print(f"{name}, your intelligence stat : {Intelligence}")

    Dexterity = random.randint(1,10)
    print(f"{name}, your dexterity stat : {Dexterity}")

    Body = random.randint(1,10)
    print(f"{name}, your body stat : {Body}")
    
