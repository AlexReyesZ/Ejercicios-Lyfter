def greet(name):
    print(f'Hello, {name}')


def repeat_twice(func):
    def wrapper(name):
        func(name)
        func(name)
    return wrapper

@repeat_twice
def greet(name):
    print(f"Hello, {name}")

# --- Testing ---
greet("Jeanca")