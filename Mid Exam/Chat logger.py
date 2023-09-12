command = input().split()
chat = []
while command[0] != "end":
    cmd = command[0]
    if cmd == "Chat":
        msg = command[1]
        chat.append(msg)
    elif cmd == "Delete":
        msg = command[1]
        if msg in chat:
            chat.remove(msg)
    elif cmd == "Edit":
        oldMsg = command[1]
        newMsg = command[2]
        if oldMsg in chat:
            index = chat.index(oldMsg)
            chat.remove(oldMsg)
            chat.insert(index, newMsg)
    elif cmd == "Pin":
        msg = command[1]
        if msg in chat:
            index = chat.index(msg)
            msg = chat.pop(index)
            chat.append(msg)
    elif cmd == "Spam":
        for i in range(1, len(command)):
            chat.append(command[i])
    command = input().split()
for message in chat:
    print(message)