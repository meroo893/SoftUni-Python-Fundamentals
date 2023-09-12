def positive_divisors(num):
    divisors = []
    for i in range(1, num//2+1):
        if num % i == 0:
            divisors.append(i)
    return divisors


n = int(input())
aliquot = sum(positive_divisors(n))
if aliquot == n:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")