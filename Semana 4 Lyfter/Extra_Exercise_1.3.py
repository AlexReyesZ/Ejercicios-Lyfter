# Exercise 3: Sum numbers from 1 to N


n=int(input("Which number do you want to use ?"))



#Validation

if n <= 0:
    print("You must enter a positive number greater than 0")
else:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print("The sum of numbers 1 to", n, "is", total_sum)  


