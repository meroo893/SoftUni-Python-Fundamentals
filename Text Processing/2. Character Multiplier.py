text = input().split()
leftside = text[0]
rightside = text[1]
total_sum = 0
difference = abs(len(leftside) - len(rightside))
left_longer = False
if len(leftside) > len(rightside):
    longer = len(leftside)
    left_longer = True
else:
    longer = len(rightside)

for i in range(longer - difference):
    total_sum += ord(leftside[i]) * ord(rightside[i])

if left_longer:
    for i in range(longer - difference, longer):
        total_sum += ord(leftside[i])
else:
    for i in range(longer - difference, longer):
        total_sum += ord(rightside[i])

print(total_sum)