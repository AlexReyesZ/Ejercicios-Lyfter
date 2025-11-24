

print('Welcome')

def filter_words(words, numbers):
    word_list_longer=[]
    word_list_shorter=[]
    for word in words:
        if len(word) > numbers:
            word_list_longer.append(word)
        else:
            word_list_shorter.append(word)

    return word_list_longer, word_list_shorter

text=input('Enter the words separated by commas: ')
words=text.split(',')

words = [word.strip().lower() for word in words]              #.strip() remove extra spaces and .lower()  converts everything to lowercase.

numbers=int(input('Enter the minimum number of letters:'))

longer_words, shorter_words= filter_words(words, numbers)


print(f'The words with more than {numbers} letters are: {longer_words}')
print(f'The words with {numbers} or fewer letters are: {shorter_words}')