import csv


file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Video_games\games.csv'

genre_count={}


try:
    with open( file_path, 'r', encoding='utf-8') as file:
        reader=csv.reader(file)
        next(reader, None) 

        for row in reader:
            if len(row)<2:
                continue

            genre=row[1].strip().capitalize()


            if genre in genre_count:
                genre_count[genre] +=1
            else:
                genre_count[genre]=1

    print('\nGenre found: ')
    for genre, counter in sorted(genre_count.items()):
        print(f'{genre}: {counter}')
except FileExistsError:
    print('Error: the file was not found. Please check the path')

except Exception as e:
    print(f' Unexpected error ocurred: {e}')
        


