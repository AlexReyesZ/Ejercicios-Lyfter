def show_message():
    message = "Hello from inside the function"
    print(message)  # This works because we are inside the function

show_message()

# Now try to access it outside
#print(message)  # This will cause an error!


#2 Global variable
counter = 10

def update_counter():
    global counter  # Declare that we want to use the global variable
    counter = counter + 5
    print("Inside the function, counter is:", counter)

update_counter()
print("Outside the function, counter is now:", counter)