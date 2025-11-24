def sum_list(numbers):
    sum_total=0
    for number in numbers:
        sum_total += number

    return sum_total


# Example list
My_list=[100,200,300,400,500]

# Call the function and store the result    
result=sum_list(My_list)

print("The sum of the list is:", result)