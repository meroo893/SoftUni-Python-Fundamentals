def loadingBar(n):
    prcnts = int(n / 10)
    if prcnts == 10:
        print(f"{n}% Complete!")
        print('[', end='')
        for _ in range(prcnts):
            print('%', end='')
        for _ in range(10-prcnts):
            print('.', end='')
        print(']')
    else:
        print('[', end='')
        for _ in range(prcnts):
            print('%', end='')
        for _ in range(10-prcnts):
            print('.', end='')
        print(']')
        print("Still loading...")

loadingBar(100)