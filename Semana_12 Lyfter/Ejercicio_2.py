def review_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError (f'Invalid input: {arg} All arguments must be numbers.')
        
        return func(*args, **kwargs)
    return wrapper

# -- Testing the decorator --


@review_numbers
def multiply(a, b, c):
    return a*b*c


# This will work perfectly
print(f"Result: {multiply(10, 2, 5)}")

# This will trigger the exception (ValueError)
try:
    print(multiply(10, "2", 5)) # Note the string "2"
except ValueError as e:
    print(f"Caught an error: {e}")