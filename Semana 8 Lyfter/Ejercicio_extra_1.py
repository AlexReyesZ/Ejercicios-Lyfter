# Step 1: Open the input file in read mode
with open(r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Strings_list\input.txt', 'r') as  input_file:
    
    # Step 2: Read all lines from the file  
    lines=input_file.readlines()

# Step 3: Remove newline characters and join lines with spaces
clean_text=' '.join(line.strip() for line in lines)


# Step 4: Open (or create) the output file in write mode
with open(r'C:\Users\LightForceCR\Desktop\Strings_list\output.txt', "w", encoding="utf-8") as output_file:


    # Step 5: Write the cleaned text in one line
    output_file.write(clean_text)

print("File processed successfully! Check output.txt")