class Car:
    def __init__(self, model: str, mileage: int, fuel: int):
        self.model = model
        self. mileage = mileage
        self.fuel = fuel

    def drive(self, distance: int, fuel_needed: int):
        if self.fuel >= fuel_needed:
            self.mileage += distance
            self.fuel -= fuel_needed
            print(f"{self.model} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

    def refuel(self, amount: int):
        if amount + self.fuel > 75:
            excess = amount + self.fuel - 75
            self.fuel = 75
            print(f"{self.model} refueled with {amount-excess} liters")
        else:
            self.fuel += amount
            print(f"{self.model} refueled with {amount} liters")

    def revert(self, amount: int):
        if self.mileage - amount < 10_000:
            self.mileage = 10_000
        else:
            self.mileage -= amount
            print(f"{self.model} mileage decreased by {amount} kilometers")

    def __repr__(self):
        return f"{self.model} -> Mileage: {self.mileage} kms, Fuel in the tank: {self.fuel} lt."


n = int(input())
cars = []
for _ in range(n):
    car = input().split("|")
    cars.append(Car(car[0], int(car[1]), int(car[2])))

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    elif command[0] == "Drive":
        model = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        for car in cars:
            if car.model == model:
                car.drive(distance, fuel)
                if car.mileage >= 100_000:
                    print(f"Time to sell the {car.model}!")
                    cars.remove(car)
    elif command[0] == "Refuel":
        model = command[1]
        amount = int(command[2])
        for car in cars:
            if car.model == model:
                car.refuel(amount)
    elif command[0] == "Revert":
        model = command[1]
        amount = int(command[2])
        for car in cars:
            if car.model == model:
                car.revert(amount)

for car in cars:
    print(car)
