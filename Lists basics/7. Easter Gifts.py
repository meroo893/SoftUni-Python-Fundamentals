gifts = input().split()
while True:
    command = input().split()
    if (command[0] + command[1]).lower() == "nomoney":
        break
    elif command[0].lower() == "outofstock":
        for i in range(len(gifts)):
            if gifts[i].lower() == command[1].lower():
                gifts[i] = "None"
    elif command[0].lower() == "required":
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]
    elif command[0].lower() == "justincase":
        gifts[-1] = command[1]
    else:
        continue

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")