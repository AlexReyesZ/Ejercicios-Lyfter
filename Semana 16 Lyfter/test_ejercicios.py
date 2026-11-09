import pytest
from bubble_sort import bubble_sort

# =============================================================================
# REQUIREMENT 1: UNIT TESTS FOR BUBBLE SORT
# =============================================================================

def test_bubble_sort_small_list():
    """1. Works with a small list."""
    data = [5, 2, 8, 1, 3]
    expected = [1, 2, 3, 5, 8]
    assert bubble_sort(data) == expected


def test_bubble_sort_large_list():
    """2. Works with a large list (more than 100 elements)."""
    large_data = list(range(150, 0, -1))
    expected_data = list(range(1, 151))
    assert bubble_sort(large_data) == expected_data


def test_bubble_sort_empty_list():
    """3. Works with an empty list."""
    assert bubble_sort([]) == []


@pytest.mark.parametrize("invalid_input", [123, "string", {"a": 1}, 45.67, None])
def test_bubble_sort_invalid_parameter_type(invalid_input):
    """4. Fails with non-list parameters by raising TypeError."""
    with pytest.raises(TypeError):
        bubble_sort(invalid_input)


# =============================================================================
# REQUIREMENT 2: 3 SUCCESS CASES FOR OTHER FUNCTIONS
# =============================================================================

def is_even(number):
    return number % 2 == 0


def count_elements(data_list):
    return len(data_list)


def convert_to_uppercase(text):
    return text.upper()


def test_is_even_success_cases():
    """3 success cases for is_even function."""
    assert is_even(2) is True   # Case 1: Positive even number
    assert is_even(0) is True   # Case 2: Zero
    assert is_even(-4) is True  # Case 3: Negative even number


def test_count_elements_success_cases():
    """3 success cases for count_elements function."""
    assert count_elements([1, 2, 3]) == 3  # Case 1: Multi-element list
    assert count_elements([]) == 0         # Case 2: Empty list
    assert count_elements(["a"]) == 1      # Case 3: Single-element list


def test_convert_to_uppercase_success_cases():
    """3 success cases for convert_to_uppercase function."""
    assert convert_to_uppercase("hello") == "HELLO"   # Case 1: Standard word
    assert convert_to_uppercase("pytest") == "PYTEST" # Case 2: Lowercase string
    assert convert_to_uppercase("a") == "A"           # Case 3: Single character