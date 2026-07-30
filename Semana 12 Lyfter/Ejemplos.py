def my_function_with_infinite_params(*args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")


my_function_with_infinite_params(
    2, 5, 6, 3, 6, 5, 6
)