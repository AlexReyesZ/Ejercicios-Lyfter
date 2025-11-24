#ask the user for 5 numbers and show the highest.

counter=1
number=int(input("Enter the first number: "))
grater= number

while counter < 5:
    counter +=1
    number=int(input("Enter the next number: "))
    if number>grater:
        grater=number

print("The greater number is : ", grater)
