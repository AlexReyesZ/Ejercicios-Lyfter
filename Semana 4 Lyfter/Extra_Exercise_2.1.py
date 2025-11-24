#secret number between 1 to 10

secret_number=7
user_attempt=int(input("Guess the number between 1 to 10: "))
if secret_number == user_attempt:
    print("Correct answer, you guess the number")

elif secret_number!=user_attempt:
    print("Incorrect answer, please try again")




