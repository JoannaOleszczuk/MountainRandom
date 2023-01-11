import random as r
# MountainList = [["Sniezka", 1602], ["Babia Gora", 1725], ["Snieznik", 1423], ["Giewont", 1895], ["Rysy", 2499], ["Kasprowy Wierch", 1987], ["Koscielec", 2155]]
MountainListFromFile = []

filepath = "MountainsList.txt"
f = open(filepath, "r")
MountainList = f.readlines()
print(MountainList)

for i in MountainList:
    i=i[:-1]
    MountainListFromFile.append(i.split(","))

counter = 0
for i in MountainListFromFile:
    MountainListFromFile[counter][1] = int(i[1])
    counter += 1
print(MountainListFromFile)

points = 0
totalLife = 3
life = 3

for i in MountainListFromFile:
    RandomValue = r.randrange(0, len(MountainListFromFile)-1)
    AskUser = (input("(Current points:" + str(points) + " , life availability: " + str(life) + "/" + str(totalLife) +") " + " What is the high of " + MountainListFromFile[RandomValue][0] + "?"))

    if int(AskUser) == MountainListFromFile[RandomValue][1]:
        print("Good answer")
        points += 1
    else:
        life -= 1
        print("Wrong answer")
        if life == 0:
            print("Game is over")
            break