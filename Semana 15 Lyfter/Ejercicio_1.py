#Complexity: O(n*m*p) (Cubic)
# Explanation: Contains three nested for loops. The outer loop iterates through list_a of size N, the middle loop iterates through list_b of size M, and the inner loop iterates through list_c of size P. 
# The total number of iterations is proportional to N * M * P. 


# -------------------------------------------------------------------
# Algorithm: Bubble Sort
# -------------------------------------------------------------------
# Complexity: O(n²) (Quadratic Time)
# 
# Explanation:
# Bubble sort uses nested loops to compare adjacent elements in an array/list
# of size N and swap them if they are in the wrong order.
# In the worst and average cases, the outer loop runs N times, and the inner
# loop runs up to N times for each iteration of the outer loop.
# This results in approximately N * N / 2 comparisons and swaps, which simplifies
# to O(n²) polynomial/quadratic complexity.
# -------------------------------------------------------------------



#print_numbers_times_2

def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)

#Complexity: O(n) (Linear)
# Explanation: Contains a single for loop that iterates through numbers_list of size N. 
# The multiplication and print operations execute a number of times directly proportional to N.

#-----------------------------------------------------------------

#check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

#Complexity: O(n*m) (Quadratic)
# Explanation: Contains a nested for loop. The outer loop iterates through list_a of size N,
#  and the inner loop iterates through list_b of size M. 
# The total number of iterations is proportional to N * M. 

#-----------------------------------------------------------------

#print_10_or_less_elements

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])

#Complexity: O(1) (Constant)
# Explanation: The function always prints at most 10 elements, regardless of the size of the input list.

#-----------------------------------------------------------------

#generate_list_trios
def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

