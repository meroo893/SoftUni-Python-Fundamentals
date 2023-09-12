text = input()
emojis = []
index = 0
for letter in text:
    index += 1
    if letter == ":":
        emojis.append(letter+text[index])

for emoji in emojis:
    print(emoji)