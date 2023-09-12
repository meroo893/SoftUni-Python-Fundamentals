import re
text = ""
total_money = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)"
while True:
    command = input()
    if command == "Purchase":
        break
    if re.match(pattern, command):
        text += command

furnitures = re.findall(pattern, text)
print("Bought furniture:")
for furniture in furnitures:
    print(furniture[0])
    total_money += float(furniture[1])*int(furniture[2])
print(f"Total money spend: {total_money:.2f}")
