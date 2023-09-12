products = input().split("|")
budget = float(input())
initial = budget
prices = []
for p in products:
    buy = False
    over_budget = True
    product = p.split("->")
    name = product[0]
    price = float(product[-1])
    if (name == "Clothes" and price <= 50.00) or (name == "Shoes" and price <= 35.00) or\
            (name == "Accessories" and price <= 20.50):
        buy = True
    if budget-price >= 0 and buy:
        budget -= price
        prices.append(price*1.4)

profit = sum(prices) + budget - initial
for price in prices:
    print(f"{price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if profit + initial >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
