class Employee:
    def __init__(self, name, salary):
        self._name=name
        self.salary=salary

# --- NAME PROPERTY ---
    @property
    def name(self):
        return self._name 
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):

        if value >=0:
            self._salary=value

        else:
            print("Error: Salary cannot be negative.")

# --- METHODS ---
    def promote(self, percentage):
        if percentage > 0:
            increase = self._salary * percentage
            # Usamos el setter para actualizar (esto activará la validación)
            self.salary = self._salary + increase
        else:
            print("El porcentaje debe ser mayor a 0.")

# Create the employee
employee=Employee('Alex', 10000)

# Apply 10% promotion
employee.promote(0.1)

#checik result
print(f'Employee: {employee.name}')
print(f'New salary: ${employee.salary:.2f}')