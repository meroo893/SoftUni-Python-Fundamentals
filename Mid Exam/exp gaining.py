expNeeded = float(input())
battles = int(input())
for battle in range(1, battles+1):
    expBattle = float(input())
    if battle % 15 == 0:
        expBattle *= 1.05
    elif battle % 5 == 0:
        expBattle *= 0.9
    elif battle % 3 == 0:
        expBattle *= 1.15
    expNeeded -= expBattle
    if expNeeded <= 0:
        break

if expNeeded <= 0:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {expNeeded:.2f} more needed.")