alpha = "QWERTYUIOPASDFGHJKLZXCVBNM"
nums = "1234567890"
valid_locations = []
cmd = input()
cmd_dashes = cmd.split("/")
cmd_equals = cmd.split("=")

while "" in cmd_dashes:
    cmd_dashes.remove("")
while "" in cmd_equals:
    cmd_equals.remove("")

if len(cmd_dashes) > len(cmd_equals):
    cmd_len = len(cmd_dashes)
else:
    cmd_len = len(cmd_equals)

for i in range(cmd_len):

    if i < len(cmd_equals):
        wordE = cmd_equals[i]
        if wordE.isalpha() and wordE[0] in alpha and len(wordE) >= 3:
            valid_locations.append(wordE)

    if i < len(cmd_dashes):
        wordD = cmd_dashes[i]
        if wordD.isalpha() and wordD[0] in alpha and len(wordD) >= 3:
            valid_locations.append(wordD)


total_points = 0
for dest in valid_locations:
    total_points += len(dest)

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {total_points}")