mats_quantity = {"shards": 0,
                 "fragments": 0,
                 "motes": 0}
completed = False
while not completed:
    mats = input().split()
    for i in range(0, len(mats), 2):
        if mats[i+1].lower() not in mats_quantity.keys():
            mats_quantity[f"{mats[i+1].lower()}"] = int(mats[i])
        else:
            mats_quantity[f"{mats[i + 1].lower()}"] += int(mats[i])

        if mats_quantity["shards"] >= 250:
            print("Shadowmourne obtained!")
            mats_quantity["shards"] -= 250
            completed = True
            break
        elif mats_quantity["fragments"] >= 250:
            print("Valanyr obtained!")
            mats_quantity["fragments"] -= 250
            completed = True
            break
        elif mats_quantity["motes"] >= 250:
            print("Dragonwrath obtained!")
            mats_quantity["motes"] -= 250
            completed = True
            break

for mat, quantity in mats_quantity.items():
    print(f"{mat}: {quantity}")

