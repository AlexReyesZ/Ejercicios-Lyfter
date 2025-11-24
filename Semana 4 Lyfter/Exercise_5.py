# Program: Calculate student grade statistics

# Initialize variables
total_grades = int(input("Enter the total number of grades: "))

passed_count = 0
failed_count = 0
sum_passed = 0
sum_failed = 0
sum_total = 0

# Loop to input all grades
#This loop repeats from 1 to total_grades.
#Each time it completes, it asks the user for a grade and converts it to a decimal number (float),
#since a grade can have decimals (e.g., 85.5).

for i in range(1, total_grades + 1):
    grade = float(input(f"Enter grade number {i}: "))



    sum_total += grade

    if grade < 70:
        failed_count += 1
        sum_failed += grade
    else:
        passed_count += 1
        sum_passed += grade

# Calculate averages safely (avoiding division by zero)
average_total = sum_total / total_grades if total_grades > 0 else 0
average_passed = sum_passed / passed_count if passed_count > 0 else 0
average_failed = sum_failed / failed_count if failed_count > 0 else 0

#if ... else 0 prevents errors if, 
# for example, there are no passing grades (you can't divide by 0).

# Show results
print("Results:")
print(f"Number of passing grades: {passed_count}")
print(f"Average of passing grades: {average_passed:.2f}")
print(f"Number of failing grades: {failed_count}")
print(f"Average of failing grades: {average_failed:.2f}")
print(f"Overall average: {average_total:.2f}")

#f-strings (e.g., f"{average_total:.2f}") allow variables to be included within the text 
#and :.2f rounds the number to two decimal places.