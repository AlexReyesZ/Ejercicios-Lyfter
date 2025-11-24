# Function to check if a number is prime

def is_prime(num):
    if num < 2:
        return False                             # 0 and 1 are not prime numbers
    for i in range(2, int(num **0.5)+1):         # Check divisors up to the square root
        if num % i ==0:
            return False
        
    return True



# Function to get all primes from a list

def get_primes(numbers):
    primes=[]
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes



# Example
list_numbers = [1,12, 23, 7, 37, 9, 78, 99]
result = get_primes(list_numbers)
print(result)