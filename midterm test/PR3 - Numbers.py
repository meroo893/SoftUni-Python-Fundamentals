numbers = list(map(int, input().split()))
avg = sum(numbers) / len(numbers)
greateravg = []
top5 = []
for number in numbers:
    if number > avg:
        greateravg.append(number)
greateravg.sort()
greateravg.reverse()

if len(greateravg) > 5:
    i = 0
    while i < 5:
        top5.append(greateravg[i])
        i += 1
else:
    top5 = greateravg

if top5:
    for number in top5:
        print(number, end=" ")
else:
    print("No")
