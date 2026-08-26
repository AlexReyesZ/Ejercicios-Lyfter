# =============================================================================
# EXERCISE 1: Sum of Natural Numbers
# =============================================================================

def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Complexity: O(n) (Linear)
# Explanation: Executes a loop 'n' times to perform the sum sequentially.


def add_formula(n):
    return n * (n + 1) // 2

# Complexity: O(1) (Constant)
# Explanation: Performs a fixed set of basic arithmetic operations regardless of 'n'.

"""
ANSWERS TO QUESTIONS:
1. What is the time complexity of each version?
   - manual_add: O(n) - Linear.
   - add_formula: O(1) - Constant.

2. Which version would you use if n = 1,000,000,000? Why?
   - Use add_formula (O(1)).
   - Reason: manual_add requires executing 1,000,000,000 loop iterations, taking
     several seconds or minutes. add_formula uses Gauss's formula and computes
     the result instantaneously in microseconds without wasting CPU resources.
"""

# -----------------------------------------------------------------------------


# =============================================================================
# EXERCISE 2: Linear Search vs Binary Search
# =============================================================================

def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

# Complexity: O(n) (Linear)
# Explanation: Scans the array element by element from start to finish in the worst case.


def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Complexity: O(log n) (Logarithmic)
# Explanation: Halves the search space with every iteration.

"""
ANSWERS TO QUESTIONS:
1. What is the complexity of each algorithm?
   - linear_search: O(n) - Linear.
   - binary_search: O(log n) - Logarithmic.

2. Under what conditions is it best to use each one?
   - linear_search: Best when the list is small, when data IS NOT sorted, 
     or for one-off searches where sorting first isn't worth the overhead.
   - binary_search: Best when the list is large and ALREADY SORTED, or when 
     performing multiple repeated searches on the same dataset.

3. What happens if the list is not sorted?
   - linear_search continues to work properly.
   - binary_search FAILS and returns incorrect results (false negatives) 
     because it assumes ordered data to safely eliminate half of the list.
"""

# -----------------------------------------------------------------------------


# =============================================================================
# EXERCISE 3: print_all_pairs
# =============================================================================

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

# Complexity: O(n^2) (Quadratic)
# Explanation: Contains two nested loops iterating over the same dictionary keys.

"""
ANSWERS TO QUESTIONS:
1. What is the time complexity?
   - O(n^2) - Quadratic (where 'n' is the number of keys in the dictionary).

2. How long does it take if there are 1 million keys?
   - For n = 1,000,000, total print operations equal n^2 = 1,000,000,000,000 (1 trillion).
   - Due to heavy I/O overhead (printing to console) and executing 1 trillion iterations, 
     the execution would take several hours to DAYS to complete.
"""