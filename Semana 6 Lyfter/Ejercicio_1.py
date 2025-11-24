def second_function():
    print("This is the second function")


def first_function():
    print("This is the first function - about to call the second")
    second_function()


first_function()
