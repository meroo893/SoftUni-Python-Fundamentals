e1 = int(input())
e2 = int(input())
e3 = int(input())
e = e1+e2+e3 #combined efficency
students = int(input())
hours = students // e #hours of work
if students % e != 0:
    hours += 1

hours += hours//4 #break every 4 hours

print(hours)