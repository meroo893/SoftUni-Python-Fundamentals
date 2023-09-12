"""
def check_even(number):
    if number % 2 == 0:
        return True
    return False

even_nums = list(filter(check_even, nums))
print(even_nums)
"""

"""
x = sorted(nums)
print(x)
"""
nums = list(map(int, input().split()))
maximum = max(nums)
minimum = min(nums)
summ = sum(nums)
print(f"""The minimum number is {minimum}
The maximum number is {maximum}
The sum number is: {summ} 
""")
