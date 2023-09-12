num_electrons = int(input())
shells = []
n = 1
while True:
    num_electrons -= 2 * n ** 2
    if num_electrons <= 0:
        num_electrons += 2 * n ** 2
        shells.append(num_electrons)
        break
    else:
        shells.append(2 * n ** 2)
    n += 1

print(shells)