# Step 1: Open the input file in read mode
with open(r'C:\Users\LightForceCR\Desktop\Programacion\week_8\SongsSorter\songs.txt', "r") as input_file:


    # Step 2: Read all lines and store them in a list
    songs = input_file.readlines()

# Step 3: Remove newline characters (\n) and extra spaces
songs = [song.strip() for song in songs]

# Step 4: Sort the list alphabetically
songs.sort()

print(songs)

# Step 5: Open another file in write mode to save the sorted songs
with open(r'C:\Users\LightForceCR\Desktop\SongsSorter\sorted_songs.txt', "w") as output_file:

    # Step 6: Write each song in a new line
    for song in songs:
        output_file.write(song + "\n")

print("Songs have been sorted and saved in 'sorted_songs.txt'")



