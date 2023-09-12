def print_nums_list(numbers):
    c = 1
    for n in numbers:
        print(f" {n}", end='')
        if c != len(numbers):
            print(',', end='')
        c += 1


nums = list(map(int, input().split(", ")))
pos = []
neg = []
even = []
odd = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

print("Positive:", end='')
print_nums_list(pos)

print("\nNegative:", end='')
print_nums_list(neg)

print("\nEven:", end='')
print_nums_list(even)

print("\nOdd:", end='')
print_nums_list(odd)