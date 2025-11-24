import csv
import os

# Step 1: Define the file path

file_path= r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Video_games\games_tab.csv'


# Step 2: Function to ensure input is not empty
def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field cannot be empty. Please try again.")
        else:
            return value
        
# Step 3: Ask how many video games to add
while True:
    try:
        n=int(input("How many video games do you want to enter: "))
        if n <=0:
            print(" You must enter at least one video game.")
        else:
            break

    except ValueError:
        print(" Please enter a valid number.")


# Step 4: Open the file in write mode (creates or overwrites)

with open (file_path, 'a', newline='', encoding='utf-8') as file:
    writer=csv.writer(file, delimiter='\t')

    # Step 5: Write header only if file is empty***
    if os.path.getsize(file_path) ==0:
        writer.writerow(['name', 'genre', 'developer', 'classification'])

    # Step 6: Loop to collect and write each video game
    for i in range(n):
        print(f"\n--- Video game {i+1} ---")
        name = get_input("Enter the name: ")
        genre = get_input("Enter the genre: ")
        developer = get_input("Enter the developer: ")
        classification = get_input("Enter the ESRB rating: ")

        # Step 7: Write the information as a new row
        writer.writerow([name, genre, developer, classification])

print(" The information has been saved successfully in games_tab.csv")