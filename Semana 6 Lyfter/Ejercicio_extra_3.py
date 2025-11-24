
def counter_vowels(words):

    words=words.lower()
    vowels='a,e,i,o,u'

    counter=0

    for word in words:
        if word in vowels:
            counter+=1
    return counter


user_text=input('Enter a text: ')
print(f'The number of vowels are:{counter_vowels(user_text)}')
