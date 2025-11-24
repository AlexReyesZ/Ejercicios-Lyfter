import csv

file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Video_games\games.csv'

try:
    with open(file_path,'r', encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader, None)

        name_dev=input('Enter the developer name: ').strip().lower()
        found_games=[]

        for row in reader:
            if len(row) < 4:
                continue

            name=row[0].strip()
            genre=row[1].strip()
            developer=row[2].strip().lower()
            classification=row[3].strip()

            if developer==name_dev:
                found_games.append((name,genre,classification))

        if found_games:
            print(f'\nVideo games developed by {name_dev.capitalize()}:')

            for game in found_games:
                print(f'- {game[0]} classification: {game[2]}, genre: {game[1]}')

        else:
            print(f'\nNo games found for developer: {name_dev.capitalize()}')

except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
