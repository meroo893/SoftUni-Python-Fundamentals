def tribonacci_rec(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    return tribonacci_rec(n-1) + tribonacci_rec(n-2) + tribonacci_rec(n-3)


def print_tribonacci(n):
    for i in range(1, n):
        if tribonacci_rec(i) != 0:
            print(f"{tribonacci_rec(i)}", end=" ")


num = int(input()) + 3
print_tribonacci(num)
