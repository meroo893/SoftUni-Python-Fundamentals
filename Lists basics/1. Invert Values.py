nums = map(int, input().split())
nums = list(nums)
for num in nums:
    p = nums.pop(0)
    p = -p
    nums.append(p)

print(nums)