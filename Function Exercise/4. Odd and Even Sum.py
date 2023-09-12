def summer(n):
    n
    even = 0
    odd = 0
    while n != 0:
        digit = n % 10
        if digit % 2 == 0:
            even += digit
        else:
            odd += digit
        n = n // 10
    print(f"Odd sum = {odd}, Even sum = {even}")


num = int(input())
summer(num)
