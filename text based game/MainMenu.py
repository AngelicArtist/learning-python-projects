
def Start_screen():
    print(f"Welcome to the Dark Forest\n")

    while True:
        choice = input("Do you wish to begin? (y/n)\n")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print("Maybe next time")
            exit()
                       
        

   