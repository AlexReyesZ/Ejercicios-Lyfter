# Lists of dictionary keys and corresponding values
employee_keys = ["first_name", "last_name", "role"]
employee_values = ["Alex", "Reyes", "Developer"]

# Create an empty dictionary to store employee information
employee_info = {}

# Fill the dictionary using a loop
for index in range(len(employee_keys)):
    current_key = employee_keys[index]
    current_value = employee_values[index]
    employee_info[current_key] = current_value

# Display the dictionary
print(employee_info)
