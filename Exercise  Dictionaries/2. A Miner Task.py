resources = {}
while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resources.keys():
        resources[f"{resource}"] = quantity
    else:
        resources[f"{resource}"] += quantity

for res, quant in resources.items():
    print(f"{res} -> {quant}")