ppl_waiting = int(input())
lift = list(map(int, input().split()))
capacity = 4 * len(lift)
enough = False
tochno = False

for index in range(len(lift)):
    ppl_getting_on = 4 - lift[index]
    ppl_waiting -= ppl_getting_on
    if ppl_waiting < 0:
        ppl_waiting += ppl_getting_on
        lift[index] += ppl_waiting
        enough = True
        break
    elif ppl_waiting == 0:
        lift[index] += ppl_getting_on
        tochno = True
        break
    else:
        lift[index] += ppl_getting_on


if enough:
    print(f"The lift has empty spots!")
    print(f"{' '.join(map(str, lift))}")
elif tochno:
    print(f"{' '.join(map(str, lift))}")
else:
    print(f"There isn't enough space! {ppl_waiting} people in a queue!")
    print(f"{' '.join(map(str, lift))}")
