import random
rand_num = random.randint(1, 100)
player_guess = int(input("Guess a number>> "))
while player_guess != rand_num:
    if player_guess > rand_num:
        print("Lower!")
    else:
        print("Higher!")
    player_guess = int(input("Guess a new number>> "))
print(f"Congratulations! You won! The mysterious number was {rand_num}")