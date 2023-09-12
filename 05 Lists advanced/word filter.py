words = input().split()
even_lengths = []
for word in words:
    if len(word) % 2 == 0:
        even_lengths.append(word)

for word in even_lengths:
    print(word)
