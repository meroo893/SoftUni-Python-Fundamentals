text = input()
ordered = []
enciphered = []
for char in text:
    ordered.append(ord(char))

for num in ordered:
    enciphered.append(chr(num+3))

print("".join(enciphered))
