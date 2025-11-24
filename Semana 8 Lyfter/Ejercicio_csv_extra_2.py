import csv

filepath=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Video_games\games.csv'

search_esrb=input('Enter the ESRB  clasification to searcg (E,T,M,etc.):').strip().upper()

found=False

with open(filepath,'r', encoding='utf-8') as file:
    reader=csv.reader(file)

    for row in reader:
        if len(row)<4:
            continue


        if row[3].strip().upper() == search_esrb:
            found=True
            print(f"\nName: {row[0]}")
            print(f"Genre: {row[1]}")
            print(f"Developer: {row[2]}")
            print(f"ESRB: {row[3]}")

if not found:
    print(f"No games found with ESRB classification '{search_esrb}'.")


