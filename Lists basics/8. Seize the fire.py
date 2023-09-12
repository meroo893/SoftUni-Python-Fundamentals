cells = input().split("#")
water = int(input())
types_of_fires = []
values_of_cells = []
for s in cells:
    cell = s.split()
    valid_fire = False
    enough_water = False
    if (cell[0] == "High" and (81 <= int(cell[-1]) <= 125)) or (cell[0] == "Medium" and (51 <= int(cell[-1]) <= 80)) or\
            (cell[0] == "Low" and (1 <= int(cell[-1]) <= 50)):
        valid_fire = True
    if water - int(cell[-1]) >= 0 and valid_fire:
        enough_water = True
        water -= int(cell[-1])
    if valid_fire and enough_water:
        types_of_fires.append(cell[0])
        values_of_cells.append(int(cell[-1]))

effort = sum(values_of_cells) * 0.25
total_fire = sum(values_of_cells)

print("Cells:")
for value in values_of_cells:
    print(f" - {value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire:.0f}")
