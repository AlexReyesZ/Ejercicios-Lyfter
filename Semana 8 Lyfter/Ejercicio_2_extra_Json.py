import json

file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Pokemon\pokemons.json'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemons_info=json.load(file)
except FileNotFoundError:
    print('File not found. Check the path')
    pokemons = []
    

def get_pok_type():
    while True:
        user_type = input("\nEnter the Pokémon type you want to search (fire, water, electric, etc): ").strip().capitalize()
        if user_type == "":   # empty input
            print("Type can not be empty, try again.")
            continue
        return user_type.capitalize()



def search_pok_type (pokemon_list, pokemon_type):
    result=[]
    for pokemon in pokemon_list:
        if pokemon_type.lower() in [ty.lower() for ty in pokemon['type']]:
            result.append(pokemon['name']['english'])
    return result



def main(pokemons_info):
    if pokemons_info:
        user_type=get_pok_type()
        found_pok=search_pok_type(pokemons_info, user_type)
        if found_pok:
            print(f"\nThe Pokémon that exist of type '{user_type}' are:")
            for names in found_pok:
                print('-', names)
        else:
            print(f"\nNo Pokémon found of type '{user_type}'.")
    else:
        print("No Pokémon data available. Please check your JSON file.")


# Run main only if this file is executed directly
if __name__ == "__main__":
    main(pokemons_info)
