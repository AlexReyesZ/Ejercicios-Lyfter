import json

file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Pokemon\pokemons.json'

# Step 2: Try to read existing data
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemons=json.load(file)
except FileNotFoundError:
    print('---File not found. Creating a new one---')
    pokemons=[]

# Function to safely get an integer input
def get_int(prompt):
    while True:
        user_value = input(prompt)
        if user_value.strip() == "":   # empty input
            print("Please enter a number, not an empty value.")
            continue
        if not user_value.isdigit():   # letters or symbols
            print("Invalid input. Please enter a valid number.")
            continue
        return (user_value)
    

# Function to safely get a name input

def get_name(prompt_2):
    while True:
        value_name = input(prompt_2)
        if value_name == "":
            print("Name cannot be empty.")
            continue
        return value_name.capitalize()
    
# Function to safely get a type input
def get_type(prompt_3):
    while True:
        value_type = input(prompt_3)
        if not value_type:
            print("Type cannot be empty.")
            continue
        return [ty.capitalize() for ty in value_type.split()]

print('Enter a new pokemon information:')


pok_name=get_name("Enter the Pokémon name (English): ")
pok_types=get_type("Enter Pokémon type(s): ")

print("\nEnter base stats:")
hp=get_int('HP: ')
attack=get_int('Attack: ')
defense=get_int('Defense: ')
sp_attack=get_int('SP Attack: ')
sp_defense=get_int('SP Defense: ')
speed=get_int('Speed: ')


# Step 4: Create new Pokémon dictionary

new_pokemon={
    "name":{"english": pok_name},
    "type":[ty.strip() for ty in pok_types],
    "base":{
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp.Attack": sp_attack,
        "Sp.Defense": sp_defense,
        "Speed": speed

    }
}

# Step 5: Add new Pokémon to list

pokemons.append(new_pokemon)

# Step 6: Save updated list to JSON file

with open(file_path,'w', encoding='utf-8') as file:
    json.dump(pokemons, file, indent=2, ensure_ascii=False)


print(f'\n {pok_name}, Has been added succesfully!')