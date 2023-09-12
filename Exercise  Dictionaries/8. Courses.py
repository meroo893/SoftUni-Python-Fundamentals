courses = {}
while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course_name = command[0]
    person = command[1]
    if course_name not in courses.keys():
        courses[f"{course_name}"] = [person]
    else:
        courses[f"{course_name}"].append(person)


for course, people in courses.items():
    print(f"{course}: {len(people)}")
    for name in people:
        print(f"-- {name}")