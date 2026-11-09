from typing import List, Union

def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Returns the sum of two numerical values."""
    return a + b


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculates the arithmetic mean of a list of numbers.
    Returns 0.0 if the list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input parameter must be a list.")
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def divide_numbers(numerator: Union[int, float], denominator: Union[int, float]) -> float:
    """
    Divides the numerator by the denominator.
    Raises TypeError if inputs are not valid numbers.
    Raises ValueError if attempting to divide by zero.
    """
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise TypeError("Both numerator and denominator must be numbers.")
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return float(numerator / denominator)