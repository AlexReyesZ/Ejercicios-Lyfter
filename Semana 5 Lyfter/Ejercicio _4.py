numbers_list = [11, 22, 33, 44, 55, 66, 77]
even_numbers = []

for number in numbers_list:
    if number % 2 == 0:
        even_numbers.append(number)

print(f'Pairs numbers: {even_numbers}')