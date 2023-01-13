
import game as g

import settings as s

def menu():

    AskUser = input("Decide if you would like to play game or change the database. Press 1 to play, press 2 to manage settings, press 0 to exit: ")
    if int(AskUser) == 1:
        g.game()
    elif int(AskUser) == 2:
        s.settings()
    elif int(AskUser) == 0:
        return 0
    else:
        print("Choose 0, 1 or 2")

menu()

