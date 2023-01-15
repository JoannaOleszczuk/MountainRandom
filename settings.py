DB_FILE_NAME = "MountainsList2.txt"

def LoadFile(filepath):
    MountainListFromFile = []
    f = open(filepath, "r")
    MountainList = f.readlines()

    for i in MountainList:
        i = i[:-1]
        MountainListFromFile.append(i.split(","))

    counter = 0
    for i in MountainListFromFile:
        MountainListFromFile[counter][1] = int(i[1])
        counter += 1

    f.close()
    return MountainListFromFile

# print(LoadFile("MountainsList2.txt"))

def settings():
    AskUser = input("Choose if you would like to add, remove or show position in database. Press 1 to add, press 2 to remove, press 3 to show")

    if int(AskUser) == 1:
        while True:
            filepath = DB_FILE_NAME
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
        AskForRemoving = input("Type the Mountain to remove it from game: ")
        tmp = LoadFile(DB_FILE_NAME)

        counter = 0
        for i in tmp:
            if AskForRemoving == i[0]:
                tmp.pop(counter)
            counter +=1
        print("Updated list: " , tmp)
        filepath = DB_FILE_NAME
        f = open(filepath, "w")

        f.write(tmp)
        f.close()


    elif int(AskUser) == 3:
        print(LoadFile(DB_FILE_NAME))