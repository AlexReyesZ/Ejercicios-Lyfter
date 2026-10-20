from datetime import datetime


def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance (arg,(int, float)):
                raise ValueError(f'Invalid input: {arg}, All inputs must be numbers')
            
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    def wrapper(*args, **kwargs):
        current_time=datetime.now()

        print(f'Func: {func.__name__}- Args: {args} - [{current_time}]')

        result=func(*args, **kwargs)
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a*b

#---Testing---

multiply(3,4)


# Try multiplying a number and a string
try:
    multiply(3, "4")
except ValueError as e:
    print(f" Error Caught: {e}")