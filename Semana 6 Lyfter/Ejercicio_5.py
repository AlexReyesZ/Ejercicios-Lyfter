def count_cases(text):

    upper_counter=0
    lower_counter=0

    for char in text:
        if char.isupper():      #returns True if the character is uppercase (A–Z).
            upper_counter += 1
        elif char.islower():   #returns True if the character is lowercase (a–z).
            lower_counter += 1

    print(f"There are {upper_counter} upper cases and {lower_counter} lower cases.")



count_cases("I want Travel around the World")



