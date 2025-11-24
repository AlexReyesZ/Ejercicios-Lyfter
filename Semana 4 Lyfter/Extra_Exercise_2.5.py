#ask the user for 100 numbers and show the sum of all of them.


sum=0
counter=1


while counter <=100:

    number=int(input("Enter a number: "))
    sum +=number
    counter +=1

print("The sum of the 100 numbers is: ",sum)

