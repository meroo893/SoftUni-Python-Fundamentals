numbers = list(map(int, input().split(", ")))
group = []
dec = 1
for dec in range(1, (max(numbers)-1)//10 + 2):
    for num in numbers:
        if (dec-1) * 10 < num <= dec*10:
            group.append(num)
    print(f"Group of {dec * 10}'s: {group}")
    group = []
