def swap(index1, index2, _self):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr


def multiply(index1, index2, arr):
    res = arr[index1] * arr[index2]
    arr[index1] = res
    return arr


def decrease(arr):
    for i in range(len(arr)):
        arr[i] -= 1
    return arr


arr = list(map(int, input().split()))
command_list = input().split()
command = command_list[0]
while command.lower() != 'end':
    if command.lower() == 'decrease':
        arr = decrease(arr)
    elif command.lower() == 'swap':
        i1 = command_list[1]
        i2 = command_list[2]
        arr = swap(i1, i2, arr)
    elif command.lower() == 'multiply':
        i1 = command_list[1]
        i2 = command_list[2]
        arr = multiply(i1, i2, arr)
    command_list = input().split()
    command = command_list[0]
    print(arr)
