nums = list(map(int, input().split()))
remove_count = int(input())
removed = []
for num in nums:
    removed.append(num)
removed.sort()
for i in range(remove_count, len(removed)):
    removed.pop(remove_count)

for num in removed:
    nums.remove(num)

for num in nums:
    if num == nums[-1]:
        break
    print(f"{num},", end=" ")
print(nums[-1])

