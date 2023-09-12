contacts = {}
while True:
    command = input()
    if command.isnumeric():
        n = int(command)
        break
    contact = command.split("-")
    contacts[contact[0]] = contact[1]

for _ in range(n):
    name = input()
    if name in contacts.keys():
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")
