# Exercise 6: Calculate percentage of women and men

total = 6
women = 0
men = 0
counter = 1

while counter <= total:
    response = int(input("Enter 1 if the person is a woman or 2 if a man: "))
    
    if response != 1 and response != 2:
        print("Enter a valid value: 1 or 2")
        continue  # Repeat this iteration without increasing counter
    
    if response == 1:
        women += 1
    elif response == 2:
        men += 1
    
    counter += 1

# Calculate percentages
percentage_women = (women / total) * 100
percentage_men = (men / total) * 100

# Output
print("\nFinal results:")
print("Percentage of women:", percentage_women, "%")
print("Percentage of men:", percentage_men, "%")