fruit = input()
day = input()
n = float(input())
valid_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
valid_fruits = ['banana', 'apple', 'orange', 'grapefruit', 'kiwi', 'pineapple', 'grapes']
if day in valid_days and fruit in valid_fruits:
    if day in workdays:
        banana = 2.5
        apple = 1.2
        orange = 0.85
        grapefruit = 1.45
        kiwi = 2.7
        pineapple = 5.5
        grapes = 3.85
    else:
        banana = 2.7
        apple = 1.25
        orange = 0.9
        grapefruit = 1.6
        kiwi = 3
        pineapple = 5.6
        grapes = 4.2

    if fruit == 'banana':
        print(f'{n * banana:.2f}')
    elif fruit == 'apple':
        print(f'{n * apple:.2f}')
    elif fruit == 'orange':
        print(f'{n * orange:.2f}')
    elif fruit == 'grapefruit':
        print(f'{n * grapefruit:.2f}')
    elif fruit == 'kiwi':
        print(f'{n * kiwi:.2f}')
    elif fruit == 'pineapple':
        print(f'{n * pineapple:.2f}')
    else:
        print(f'{n * grapes:.2f}')
else:
    print('error')