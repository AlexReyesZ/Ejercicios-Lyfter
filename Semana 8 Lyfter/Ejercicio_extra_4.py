# Step 1: Ask the user for a line of text

user_text=input('Enter a line of text to add: ')

# Step 2: Define the file path

file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\User_log\logs.txt'


# Step 3: Open the file in append mode ('a') / If the file does not exist, it will be created automatically
with open(file_path, 'a', encoding='utf-8') as file:
    file.write(user_text + '\n')


print("The text was added successfully to the file.")