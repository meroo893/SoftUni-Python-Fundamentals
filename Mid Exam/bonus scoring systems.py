rooms = input().split("|")
health = 100
bitcoin = 0
room_counter = 1
dead = False
for room in rooms:
    amount = int(room.split()[1])
    mob = room.split()[0]
    if mob == "potion":
        if health + amount > 100:
            amount = 100 - health
        health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif mob == "chest":
        bitcoin += amount
        print(f"You found {amount} bitcoins.")
    else:
        health -= amount
        if health <= 0:
            dead = True
            break
        if not dead:
            print(f"You slayed {mob}.")
    room_counter += 1

if dead:
    print(f"You died! Killed by {mob}.")
    print(f"Best room: {room_counter}")
else:
    print(f"""You've made it!
Bitcoins: {bitcoin}
Health: {health}""")