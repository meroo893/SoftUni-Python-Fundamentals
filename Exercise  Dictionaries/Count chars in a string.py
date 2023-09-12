text = input()
chars = {}
for char in text:
    if char != " ":
        chars[f'{char}'] = 0
for char in text:
    if char != " ":
        chars[f'{char}'] += 1

for char, occurrences in chars.items():
    print(f"{char} -> {occurrences}")