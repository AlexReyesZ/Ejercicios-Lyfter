def trace(func):
    def wrapper(*args, **kwargs):
        print(f' DEBUG: Calling {func.__name__}')
        print(f'  Imputs: {args} {kwargs}')


        result= func(*args, **kwargs)

        print(f'Debug: Result {result}')
        return result

    return wrapper


@trace
def multiply(a, b):
    return a * b

@trace
def greet(name, uppercase=False):
    if uppercase:
        return f"HELLO {name.upper()}"
    return f"Hello {name}"

multiply(8, 4)
greet("Alex", uppercase=True)