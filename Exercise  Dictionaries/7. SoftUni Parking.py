n = int(input())
registered = {}
for _ in range(n):
    command = input().split()
    if command[0].lower() == "register":
        username = command[1]
        license_plate = command[2]
        if username in registered.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            registered[f"{username}"] = license_plate
            print(f"{username} registered {license_plate} successfully")
    else:
        username = command[1]
        if username in registered.keys():
            registered.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for user, plate in registered.items():
    print(f"{user} => {plate}")