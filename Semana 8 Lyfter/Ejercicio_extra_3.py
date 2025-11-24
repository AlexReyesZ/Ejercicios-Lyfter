
file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\capital letter\text_capital_letter.txt'

with open(file_path, 'r', encoding='utf-8') as input_file:
    capital_letters=input_file.read()


upper_words=[letter.upper() for letter in capital_letters ]


with open(r'C:\Users\LightForceCR\Desktop\capital letter\output_capital_letter.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(upper_words)


print(" File processed successfully! Check output.txt")