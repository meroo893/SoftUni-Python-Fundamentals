coins = 100
energy = 100
days = input().split("|")
while "" in days:
    days.remove("")
handled = True
if len(days) != 0:
    for d in days:
        day = d.split("-")
        event = day[0]
        points = int(day[-1])
        if event == "rest":
            energy += points
            if energy > 100:
                gained_energy = 100 - energy + points
                energy = 100
                print(f"You gained {gained_energy} energy.")
                print(f"Current energy: {energy}.")
                continue
            print(f"You gained {points} energy.")
            print(f"Current energy: {energy}.")
        elif event == "order":
            if energy >= 30:
                energy -= 30
                coins += points
                print(f"You earned {points} coins.")
            else:
                energy += 50
                print("You had to rest!")
        else:
            if coins >= points:
                coins -= points
                print(f"You bought {event}.")
            else:
                print(f"Closed! Cannot afford {event}.")
                handled = False
                break
if handled:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
