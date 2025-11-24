word_list=[]

for i in range(5):
    user_word=input("Enter your word:")
    word_list.append(user_word)

#create a new list for long words

long_words=[]

for current_word in word_list:
    if len(current_word) > 4:
        long_words.append(current_word)

print(f'Words with more than 4 letters:{long_words}')

