#prompt the user for 3 numbers

number_1=int(input("Enter the first number: "))
number_2=int(input("Enter the second number: "))
number_3=int(input("Enter th third number: "))
sum=0

if number_1==30 or number_2==30 or number_3==30:
    print("CORRECT")

else:
    sum =number_1 + number_3 + number_3
    if sum==30:
        print("CORRECT")

    else:
        print("Incorrect")