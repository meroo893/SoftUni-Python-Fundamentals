def is_palindrome(num):
    backwards = ""
    for i in range(len(num)-1, -1, -1):
        backwards += num[i]
    if backwards == num:
        return True
    return False


nums = input().split(", ")
for n in nums:
    print(is_palindrome(n))
