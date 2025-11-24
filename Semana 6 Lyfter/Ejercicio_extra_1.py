def count_character(char, text):

    counter=0
    for letter in text:
        if letter.lower()==char.lower():
            counter +=1
    return counter

text=input('Enter a text: ')
char=input('Enter the character of you want to find: ')

result=count_character(char, text)

print(f'The result is: {result}')