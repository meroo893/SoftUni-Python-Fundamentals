message = input()
message_list = []

for letter in message:
    message_list.append(letter)

while True:
    command = input().split(":|:")
    if command[0] == "Reveal":
        break
    elif command[0] == "InsertSpace":
        index = int(command[1])
        message_list.insert(index, " ")
        message = "".join(message_list)
        print(message)
    elif command[0] == "Reverse":
        substring = command[1]
        index = 0
        if substring in message:
            for i in range(len(message_list) - len(substring)):
                if message[i+1:i+len(substring)+1] == substring:
                    index = i+1
                    break
            for _ in range(len(substring)):
                message_list.pop(index)
            for i in range(len(substring)-1, -1, -1):
                message_list.append(substring[i])
            message = "".join(message_list)
            print(message)
        else:
            print("error")
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        message_list.clear()
        for letter in message:
            message_list.append(letter)
        print(message)

print(f"You have a new text message: {message}")