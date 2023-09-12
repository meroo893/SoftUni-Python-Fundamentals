message = input()
message_list = []

for letter in message:
    message_list.append(letter)

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    elif command[0] == "Move":
        n = int(command[1])
        for letter in message[:n]:
            message_list.append(letter)
        for _ in range(n):
            message_list.pop(0)
        message = "".join(message_list)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message_list.insert(index, value)
        message = "".join(message_list)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
        message_list.clear()
        for letter in message:
            message_list.append(letter)

print(f"The decrypted message is: {message}")