name = input()
voldemort = False
while name.title() != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        voldemort = True
        break
    if len(name) < 5:
        house = "Gryffindor"
        print(f"{name} goes to {house}.")
    elif len(name) == 5:
        house = "Slytherin"
        print(f"{name} goes to {house}.")
    elif len(name) == 6:
        house = "Ravenclaw"
        print(f"{name} goes to {house}.")
    else:
        house = "Hufflepuff"
        print(f"{name} goes to {house}.")
    name = input()
if not voldemort:
    print("Welcome to Hogwarts.")