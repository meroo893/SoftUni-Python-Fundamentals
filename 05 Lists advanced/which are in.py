words = input().split(', ')
strings = input().split(', ')
substrings = []
for word in words:
    for string in strings:
        if word in string and word not in substrings:
            substrings.append(word)

print(substrings)
