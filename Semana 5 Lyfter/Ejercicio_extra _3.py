# ask the user for 5 numbers

number_list=[]

for i in range(10):
    user_number=int(input("Enter a number:"))
    number_list.append(user_number)


# start with the first number as the smallest    

smaller_number=number_list[0]

# compare one by one

for current_number in number_list:
    if current_number< smaller_number:
        smaller_number=current_number

print("The smaller number is:", smaller_number)
