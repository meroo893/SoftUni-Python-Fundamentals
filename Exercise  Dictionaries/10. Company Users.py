employees = {}
while True:
    command = input()
    if command.lower() == "end":
        break
    command = command.split(" -> ")
    company = command[0]
    id = command[1]
    if company not in employees.keys():
        employees[f"{company}"] = [id]
    elif id not in employees[company]:
        employees[f"{company}"].append(id)

for company, ids in employees.items():
    print(f"{company}")
    for id in ids:
        print(f"-- {id}")
