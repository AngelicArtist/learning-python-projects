def Start_screen():

    print(f"Welcome to a short story\n")

    while True:
        choice = input("Do you wish to begin? (y/n)\n")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print("Maybe next time")
            exit()

def gameover():
    exit()
# try an add a saved game function                       
        
if __name__ == "__main__":
    Start_screen()   

