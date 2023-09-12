deck = input().split()
deck_count = len(deck)
shuffle_count = int(input())
upper = []
lower = []
shuffled = []

for _ in range(shuffle_count):
    upper.clear()
    lower.clear()
    for i in range(int(len(deck) / 2)):
        upper.append(deck[i])
        lower.append(deck[i + int(len(deck) / 2)])
    deck.clear()
    for k in range(int(deck_count/2)):
        deck.append(upper[k])
        deck.append(lower[k])


print(deck)