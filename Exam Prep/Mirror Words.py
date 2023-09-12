import re
pairs = []
text = input()
pattern = r"#([A-Za-z]{3,}##[A-Za-z]{3,})#|@([A-Za-z]{3,}@@[A-Za-z]{3,})@"

words = re.findall(pattern, text)
for word in words:
    if word[0] != "":
        left = []
        right = []
        #left = word[0][:(len(word[0])//2)-1]
        for letter in word[0][:(len(word[0])//2)-1]:
            left.append(letter)
        for letter in word[0][(len(word[0])//2)+1:]:
            right.append(letter)
        right.reverse()
        if left == right:
            right.reverse()
            pair = ("".join(left), "".join(right))
            pairs.append(pair)
    else:
        left = []
        right = []
        # left = word[0][:(len(word[0])//2)-1]
        for letter in word[1][:(len(word[1]) // 2) - 1]:
            left.append(letter)
        for letter in word[1][(len(word[1]) // 2) + 1:]:
            right.append(letter)
        right.reverse()
        if left == right:
            right.reverse()
            pair = ("".join(left), "".join(right))
            pairs.append(pair)


if len(words):
    print(f"{len(words)} word pairs found!")
else:
    print(f"No word pairs found!")

if len(pairs):
    print("The mirror words are:")
    for pair in pairs:
        print(f"{pair[0]} <=> {pair[1]}", end="")
        if pair != pairs[-1]:
            print(", ", end="")
else:
    print("No mirror words!")
