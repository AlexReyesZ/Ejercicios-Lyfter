def sum_values(list):

    total_sum=0

    print('The results are:')
    for element in list:
        try:
            value=float(element)
            total_sum+=value
            print(f'{value} was added correctly')

        except ValueError:
            print(f'Invalid element: {element}')





list=['10', 'hello','3.14', 'ten', 'n/a']

sum_values(list)