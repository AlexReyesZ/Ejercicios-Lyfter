number_list = []  

# ask the user for 10 numbers
for index in range(10):
    user_number = int(input("Enter a number: "))
    number_list.append(user_number)

# find the highest number 

highest_number = number_list[0]
for current_number in number_list:
    if current_number > highest_number:
        highest_number = current_number

print("You entered:", number_list)
print("The highest number was:", highest_number)
