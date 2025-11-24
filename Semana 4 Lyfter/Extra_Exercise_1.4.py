# Exercise 4: Order two numbers from smallest to largest

# Input
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

# Swap if necessary
if first > second:
    temp = first
    first = second
    second = temp

# Output
print("The numbers in ascending order are:", first, "and", second)