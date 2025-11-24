#ask for user number

number_list=[]


for i in range(10):
    user_number=int(input("Enter a number:"))
    number_list.append(user_number)

#ask for the number to search

search_number=int(input("Enter the number of you want to search: "))

#count how many time it appears

count=0

for current_number in number_list:
    if current_number==search_number:
        count+=1


print("The number", search_number, "appears", count, "times")