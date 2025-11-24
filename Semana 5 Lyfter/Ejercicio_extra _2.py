# ask the user to enter 5 numbers

number_list=[]

for i in range(5):
    user_number=int(input("Enter your number:"))
    number_list.append(user_number)

# variable to keep track if all are positive
all_positives=True

# go through each number

for current_number in number_list:
    if current_number <=0:
        all_positives=False
        break


#Show the result

if all_positives:
    print("All number are positives.")

else:
    print("There is at least one negative number or zero")    

