employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofia", "email": "sofia@empresa.com", "department": "RH"},
]


employees_list={}



# Loop through each employee in the list
for employee in employees:
    department = employee["department"]
    if department not in employees_list:
        employees_list[department]= []   # If the department does not exist in the dictionary, initialize it with an empty list

    employees_list[department].append(employee)  # Add the employee to the correct department list

for department, employees_in_dept in employees_list.items():
    print(f"Department: {department}")
    for emp in employees_in_dept:
        print(f"  - {emp['name']} ({emp['email']})")

