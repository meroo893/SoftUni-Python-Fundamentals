products = {}
while True:
    command = input()
    if command == "buy":
        break
    product = command.split()
    name = product[0]
    price = float(product[1])
    quantity = int(product[2])
    if name not in products.keys():
        products[f"{name}"] = [price, quantity]
    else:
        old_quantity = products[f"{name}"][-1]
        products[f"{name}"] = [price, old_quantity + quantity]

for prod, total_price_list in products.items():
    total_price = total_price_list[0] * total_price_list[1]
    print(f"{prod} -> {total_price:.2f}")
