#Exercise 4: Finding the largest of three numbers

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

largest_number = first_number

if second_number > largest_number:
    largest_number = second_number

if third_number > largest_number:
    largest_number = third_number

print(f"The greatest number is: {largest_number}")