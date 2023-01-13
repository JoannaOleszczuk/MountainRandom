

def settings():
    AskUser = input("Choose if you would like to add position to database or just show it. Press 1 to add, press 2 to show")

    if int(AskUser) == 1:
        while True:
            filepath = "MountainsList.txt"
            f = open(filepath, "a")
            mountain = input("Type name of the mountain: ")
            high = input("Type high of the mountain: ")
            L = [mountain + ", " + high + "\n"]
            f.writelines(L)
            f.close()

            decision = input("Press 0 to exit or 1 to continue: ")
            if int(decision) == 0:
                break
            elif int(decision) == 1:
                continue

    elif int(AskUser) == 2:
        MountainListFromFile = []
        filepath = "MountainsList.txt"
        f = open(filepath, "r")
        MountainList = f.readlines()

        for i in MountainList:
            i = i[:-1]
            MountainListFromFile.append(i.split(","))

        counter = 0
        for i in MountainListFromFile:
            MountainListFromFile[counter][1] = int(i[1])
            counter += 1

        print(MountainListFromFile)
        f.close()