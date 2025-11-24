

import sys
#Ask the user for their name and validate it.
def get_names():
    while True:
        user_name=input('\nEnter Your Name: ')
        if user_name.isdigit():
            raise ValueError('The name can not be a number. Try again')
        elif user_name=="":
            print('The name can not be empty')
        else:
            return user_name
        





#Ask the user for their age and validate it.
def get_ages():
    user_age=input('\nEnter your age: ')
    try:
        age=int(user_age)
        return age
    except ValueError as ex:
        raise ValueError('Invalid Number. Try again')
    






#Main program that calls the functions and handles errors.
def main():
    while True:
        try:
            user_name=get_names()
            break
        except ValueError as ex:
            print(ex)


    while True:
        try:
            user_age=get_ages()
            break
        except ValueError as ex:
            print(ex)
    
    print(f'Hello {user_name},\nYour age is: {user_age}')


if __name__ == "__main__":
    main()
