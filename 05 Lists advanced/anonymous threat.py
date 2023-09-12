info = input().split()
command = input().split()
result = ''
while command[0] != '3:1':
    if command[0] == 'merge':
        start = int(command[1])
        end = int(command[2])
        if start < 0:
            start = 0
        if end > len(info) - 1:
            end = len(info) - 1
        for index, string in enumerate(info):
            if index in range(start + 1, end + 1):
                info[start] += info[index]
        for index in range(end, start, - 1):
            info.pop(index)

    elif command[0].lower() == 'divide' and int(command[2]) != 0:
        index = int(command[1])
        partitions = int(command[2])
        if partitions > len(info[index]):
            step = 1
        else:
            step = len(info[index]) // partitions
        divide_part = info.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                info.insert(index, divide_part[start::])
                break
            else:
                info.insert(index, divide_part[start: start + step:])
            start += step
            index += 1
    command = input().split()

print(' '.join(info))
