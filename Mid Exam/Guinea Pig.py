food = float(input())*1000
hay = float(input())*1000
cover = float(input())*1000
weight = float(input())*1000
enough = True
for day in range(1, 31):
    if food - 300 >= 0:
        food -= 300
    else:
        enough = False
        break
    if day % 2 == 0:
        if hay - food * 0.05 >= 0:
            hay -= food * 0.05
        else:
            enough = False
            break
    if day % 3 == 0:
        if cover - weight / 3 >= 0:
            cover -= weight / 3
        else:
            enough = False
            break
if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")
else:
    print("Merry must go to the pet store!")
