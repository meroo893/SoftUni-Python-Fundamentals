import re
text = ""
pattern = r"\d+"
while True:
    inpt = input()
    if inpt == "":
        break
    text += inpt
nums = re.findall(pattern, text)
for num in nums:
    print(num, end=" ")