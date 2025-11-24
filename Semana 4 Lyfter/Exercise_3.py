#Generate a random secret number between 1 and 10

import random

secret_number = random.randint(1, 10)
player_guess = None

print("Welcome to the Secret Number Game!")
print("Guess the secret number between 1 and 10.")

while player_guess != secret_number:
    try:
        player_guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number between 1 and 10.")
        continue

    if player_guess < 1 or player_guess > 10:
        print("The number must be between 1 and 10. Try again.")
        continue

    if player_guess < secret_number:
        print("Too low, try again.")
    elif player_guess > secret_number:
        print("Too high, try again.")
    else:
        print("CORRECT! You guessed the number!")


        












