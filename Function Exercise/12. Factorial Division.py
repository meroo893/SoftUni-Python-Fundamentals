def factorial(factor):
    if factor == 1 or factor == 0:
        return 1
    elif factor > 1:
        return factor * factorial(factor-1)
    else:
        return factor * factorial(factor + 1)


f = int(input())
divider = int(input())

print(f"{factorial(f)/factorial(divider):.2f}")
