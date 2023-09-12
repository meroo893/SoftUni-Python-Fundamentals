n1, n2, n3 = map(int, input().split('.'))
old_version = [n1, n2, n3]
n3 += 1
if n3 == 10:
    n2 += 1
    n3 = 0
if n2 == 10:
    n1 += 1
    n2 = 0

print(f"{n1}.{n2}.{n3}")