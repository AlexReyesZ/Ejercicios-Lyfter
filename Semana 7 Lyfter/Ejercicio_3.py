def convert_to_integer(my_list):
    print('result: ')
    for element in my_list:
        try:
            number=int(element)
            print(f'"{element}" convert to {number}')

        except ValueError:
            print(f'This element can not be convert: {element}')



my_list=['1','five','hello','100','string','3.14']

convert_to_integer(my_list)