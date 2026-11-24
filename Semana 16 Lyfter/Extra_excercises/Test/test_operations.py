import pytest
from operation import add_numbers, calculate_average, divide_numbers

class TestMathOperations:
    """Comprehensive test suite for arithmetic operations."""

    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 8),          # Positive numbers
        (-5, -3, -8),       # Negative numbers
        (0, 0, 0),          # Zeros
        (10, -5, 5),        # Mixed numbers
    ])
    def test_add_numbers(self, a, b, expected):
        assert add_numbers(a, b) == expected

    @pytest.mark.parametrize("numbers, expected", [
        ([10, 20, 30], 20.0),       # Positive numbers average
        ([-10, -20, -30], -20.0),   # Negative numbers average
        ([0, 0, 0], 0.0),           # Zero-only list
        ([], 0.0),                  # Empty list edge case
    ])
    def test_calculate_average(self, numbers, expected):
        assert calculate_average(numbers) == expected

    def test_calculate_average_invalid_type(self):
        with pytest.raises(TypeError) as exc_info:
            calculate_average("invalid_type")
        
        assert str(exc_info.value) == "Input parameter must be a list."


class TestDivisionOperations:
    """Test suite for division logic and exception validation."""

    @pytest.mark.parametrize("numerator, denominator, expected", [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (-10, 2, -5.0),
        (0, 4, 0.0),
    ])
    def test_divide_success(self, numerator, denominator, expected):
        assert divide_numbers(numerator, denominator) == expected

    def test_divide_by_zero(self):
        with pytest.raises(ValueError) as exc_info:
            divide_numbers(10, 0)
        
        assert str(exc_info.value) == "Cannot divide by zero."

    @pytest.mark.parametrize("numerator, denominator", [
        (10, "2"),
        ("10", 2),
        ("10", "2"),
    ])
    def test_divide_invalid_type(self, numerator, denominator):
        with pytest.raises(TypeError) as exc_info:
            divide_numbers(numerator, denominator)
        
        assert str(exc_info.value) == "Both numerator and denominator must be numbers."