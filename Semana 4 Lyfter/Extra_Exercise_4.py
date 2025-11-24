# Custom multiplication table

number = int(input("Enter a number (1 to 10): "))


if number < 1 or number > 10:
    print("Please enter a number between 1 and 10.")
else:
    for i in range(1, 13):  # from 1 to 12
        result = number * i
        print(number, "x", i, "=", result)