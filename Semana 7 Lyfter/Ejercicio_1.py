# Simple Command-Line Calculator (with functions)

def show_menu(current_number):
    print(f"Current number: {current_number}")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")



#Asks the user to choose an option.
def get_option():
    return input("Choose an option (1-6): ")   
            



#Asks the user for a number and validates it.
def get_number():                                          
    try:
        return float(input("Enter a number: "))
    except ValueError as ex:
        print(" Error: you must enter a valid number.", ex)
        return None



#math operation based on the chosen option.

def sum_operation(current_number, new_number):  
        return current_number + new_number
    
def sub_operation(current_number, new_number):
        return current_number - new_number


def mul_operation(current_number, new_number):
    return current_number * new_number


def div_operation(current_number, new_number):
    if new_number == 0:
        print("Error: cannot divide by zero.")
        return current_number
    return current_number / new_number



#Main function that runs the calculator.
def calculator():                                       
    current_number = 0

    while True:
        show_menu(current_number)
        option = get_option()

        if option == "6":
            print(" Goodbye!")
            break

        if option not in ["1", "2", "3", "4", "5"]:
            print(" Error: invalid option. Try again.")
            continue

        if option == "5":
            current_number = 0
            print("Result cleared.")
            continue

        new_number = get_number()
        if new_number is None:
            continue  # Go back to the menu if the number was invalid

        if option == "1":
            current_number = sum_operation(current_number, new_number)
        elif option == "2":
            current_number = sub_operation(current_number, new_number)
        elif option == "3":
            current_number = mul_operation(current_number, new_number)
        elif option == "4":
            current_number = div_operation(current_number, new_number)

        print(f"Result: {current_number}")


# 🔹 Start the program
calculator()


