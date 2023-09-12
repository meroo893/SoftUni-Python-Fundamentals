nums = list(map(int, input().split(", ")))
beggars_count = int(input())
beggars = []
beggar_index = 0
for _ in range(beggars_count):
    beggars.append(0)

for i in range(len(nums)):
    beggars[beggar_index] += nums[i]
    beggar_index += 1
    if beggar_index >= beggars_count:       #reseting the beggar index
        beggar_index = 0

print(beggars)