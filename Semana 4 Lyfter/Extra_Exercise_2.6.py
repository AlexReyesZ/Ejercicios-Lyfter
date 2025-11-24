#ask the user for 100 numbers and display the largest of all.

counter=1
greater=0

while counter <=5:
    number=int(input("Enter a number: "))
    if number>greater:
        greater=number
        counter +=1

print("The greatest of the 100 numbers is:", greater)


