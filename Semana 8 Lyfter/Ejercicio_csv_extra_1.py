import csv

filepath=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Video_games\games.csv'

with open (filepath, 'r', encoding='utf-8') as file:
    reader=csv.reader(file)
    

    for row in reader:
        print(f'Name: {row[0]}')
        print(f'Genre: {row[1]}')
        print(f'Developer: {row[2]}')
        print(f'ESRB: {row[3]},\n')