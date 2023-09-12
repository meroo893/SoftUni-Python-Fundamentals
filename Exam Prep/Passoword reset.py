raw_pass = input()
curr_pass = []

for let in raw_pass:
    curr_pass.append(let)

while True:
    command = input().split()
    if command[0] == "Done":
        break
    elif command[0] == "TakeOdd":
        odd = []
        for index in range(1, len(curr_pass), 2):     #REMOVES EVEN INDEXED LETTERS FROM THE LIST
            odd.append(curr_pass[index])
        curr_pass = odd
        print("".join(curr_pass))

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        for _ in range(length):
            curr_pass.pop(index)
        print("".join(curr_pass))

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        password = "".join(curr_pass)
        curr_pass.clear()
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
        for let in password:
            curr_pass.append(let)

print(f"Your password is: {''.join(curr_pass)}")