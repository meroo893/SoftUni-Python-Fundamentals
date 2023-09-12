rooms = int(input())
chairs = 0
total_free_chairs = 0
enough_chairs = True
for room in range(1, rooms+1):
    command = input().split()
    chairs = len(command[0])
    chairs_needed = int(command[1])
    free_chairs = chairs - chairs_needed
    total_free_chairs += free_chairs
    if free_chairs < 0:
        enough_chairs = False
        print(f"{abs(free_chairs)} more chairs needed in room {room}")

if enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")