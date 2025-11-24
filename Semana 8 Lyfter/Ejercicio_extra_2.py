
file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Count_words\text_input.txt'

with open (file_path, 'r', encoding='utf-8') as file:

    words_counted=file.read()



count_text=words_counted.split()

words_counted=len(count_text)

print(f'This file content: {words_counted} words')