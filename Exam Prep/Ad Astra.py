import re
products = []
calories = []
exp_dates = []
txt = input()

pattern = r"\|([A-Za-z ]+)\|(\d\d\/\d\d\/\d\d)\|(\d+)\||#([A-Za-z ]+)#(\d\d\/\d\d\/\d\d)#(\d+)#"
product_pattern = r"\|([A-Za-z ]+)\|||#([A-Za-z ]+)#"
calories_pattern = r"\|(\d+)\||#(\d+)#"
exp_date_pattern = r"\|(\d\d\/\d\d\/\d\d)\||#(\d\d\/\d\d\/\d\d)#"

matches = re.findall(pattern, txt)


for match in matches:
    if match[0] == '':
        products.append(match[-3])
        calories.append(int(match[-1]))
        exp_dates.append(match[-2])
    else:
        products.append(match[0])
        calories.append(int(match[2]))
        exp_dates.append(match[1])

days = int(sum(calories)//2000)

print(f"You have food to last you for: {days} days!")
for i in range(len(products)):
    print(f"Item: {products[i]}, Best before: {exp_dates[i]}, Nutrition: {calories[i]}")
