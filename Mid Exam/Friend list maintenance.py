names = input().split(", ")
blacklisted = []
lostNames = []
lostIndex = []
command = input().split()
    #   /////////BLACKLIST COMMAND////////////////////////////////////////
while command[0] != "Report":
    cmd = command[0]
    if cmd == "Blacklist":
        name = command[-1]
        if name in names:
            index = names.index(name)
            lost = False
            for i in lostIndex:
                if i == index:
                    lost = True
            if not lost:
                blacklisted.append(name)
                print(f"{name} was blacklisted.")
                names.remove(name)
                names.insert(index, "Blacklisted")
        else:
            print(f"{name} was not found.")
    #   /////////ERROR COMMAND////////////////////////////////////////
    elif cmd == "Error":
        index = int(command[-1])
        lost = False
        if 0 <= index < len(names):
            for i in lostIndex:
                if i == index:
                    lost = True
            if not lost and names[index] != "Blacklisted":
                print(f"{names[index]} was lost due to an error.")
                lostIndex.append(index)
                lostNames.append(names[index])
                names.pop(index)
                names.insert(index, "Lost")
    # //////////CHANGE COMMAND///////////////////////////////////////
    elif cmd == "Change":
        index = int(command[1])
        newName = command[2]
        if 0 <= index < len(names):
            print(f"{names[index]} changed his username to {newName}.")
            names.pop(index)
            names.insert(index, newName)
    command = input().split()
print(f"Blacklisted names: {len(blacklisted)}")
print(f"Lost names: {len(lostNames)}")
print(f"{' '.join(names)}")