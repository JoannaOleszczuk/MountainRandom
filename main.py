import random as r
MountainList = [["Sniezka", 1602], ["Babia Gora", 1725], ["Snieznik", 1423], ["Giewont", 1895], ["Rysy", 2499], ["Kasprowy Wierch", 1987], ["Koscielec", 2155]]
points = 0
totalLife = 3
life = 3

for i in MountainList:
    RandomValue = r.randrange(0, len(MountainList)-1)
    AskUser = (input("(Current points:" + str(points) + " , life availability: " + str(life) + "/" + str(totalLife) +") " + " What is the high of " + MountainList[RandomValue][0] + "?"))

    if int(AskUser) == MountainList[RandomValue][1]:
        print("Good answer")
        points += 1
    else:
        life -= 1
        print("Wrong answer")
        if life == 0:
            print("Game is over")
            break