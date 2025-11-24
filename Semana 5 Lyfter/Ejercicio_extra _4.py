# ask the user for 5 numbers
number_list = []
for index in range(5):
    user_number = int(input("Enter a number: "))
    number_list.append(user_number)

# calculate the total sum
total_sum = 0
for current_number in number_list:
    total_sum += current_number

# calculate the average
average = total_sum / len(number_list)

# find numbers greater than average
greater_numbers = []
for current_number in number_list:
    if current_number > average:
        greater_numbers.append(current_number)

print("Average:", average)
print("Numbers greater than average:", greater_numbers)
