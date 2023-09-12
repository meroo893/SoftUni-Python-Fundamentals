"""students = {}
n = int(input())
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[f"{name}"] = [grade]
    else:
        students[f"{name}"].append(grade)

for student, grades in students.items():
    average = sum(grades)/len(grades)
    if average < 4.5:
        continue
    print(f"{student} -> {average:.2f}")"""

emp = {'SoftUni': ['AA12345', 'CC12344'], 'Lenovo': ['XX23456']}
id = 'AA12345'
print(emp.values())