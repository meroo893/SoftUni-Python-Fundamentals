energy = int(input())
distance = input()
energy_finish = False
battles_won = 0
while distance != "End of battle":
    distance = int(distance)
    if energy - distance < 0:
        energy_finish = True
        break
    energy -= distance
    battles_won += 1
    if battles_won % 3 == 0:
        energy += battles_won
    distance = input()

if energy_finish:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")