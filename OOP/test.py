class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def greeting(self):
        return f"Hello {self.name} {self.last_name}"


n = "Mert"
ln = "Kamberov"

p1 = Person(n, ln)

p1.name = "Merve"

print(p1.greeting())