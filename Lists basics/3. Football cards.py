A_count = 11
B_count = 11
termination = False
sent_offs = set(input().split())
for sent_off_plyr in sent_offs:
    if sent_off_plyr[0] == "A":
        A_count -= 1
        if A_count < 7:
            termination = True
            break
    else:
        B_count -= 1
        if B_count < 7:
            termination = True
            break

print(f"Team A - {A_count}; Team B - {B_count}")
if termination:
    print("Game was terminated")