command = input()
destinations = []
t = 0
while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        place = command[2]
        if 0 <= index < len(destinations):
            for i in range(len(place), 1, -1):
                destinations[index] = place[i]
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        word_length = end_index - start_index
        if len(destinations) >= end_index > start_index >= 0:
            for _ in range(word_length):
                destinations.pop(start_index)
    elif command[0] == 'Switch':
        old_str = command[1]
        new_str = command[2]
        for i in range(len(destinations) - len(old_str)):
            if destinations[i:i+len(old_str)] == old_str:
                for _ in range(len(old_str)):
                    destinations.pop(i)
                for letr in range(len(new_str)):
                    destinations.insert(i, new_str[letr])
    else:
        i = 0
        for letter in "".join(command):
            destinations[i] = letter
            i += 1
    if t:
        print("".join(destinations))
    command = input()
    t = 1

print("Ready for world tour! Planned stops:")
print("".join(destinations))