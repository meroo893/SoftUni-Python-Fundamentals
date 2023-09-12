import re
pattern = r"^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+$"

n = int(input())

for _ in range(n):
    text = input()
    group = "00"
    match = re.search(pattern, text)
    if match:
        if re.search(r"\d", text):
            group = re.findall(r"\d", text)
        print(f"Product group: {''.join(group)}")
    else:
        print("Invalid barcode")
