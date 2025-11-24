import json



#Function to load the Pokémon JSON file
def load_pok(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('File not found. Check the path')
        return []
    except json.JSONDecodeError:
        print('ERROR: --File json is not valid--')
        return[]



def show_pok_info(pokemon_list):
    if not pokemon_list:
        print("No Pokémon data available.")
        return
    

    print('--Pokemon list--')
    for pokemon in pokemon_list:
        name=pokemon['name'].get('english','unknow')
        types=','.join(pokemon.get('type', []))
        base=pokemon.get('base',{})
        attack=base.get('Attack', 0)
        defense=base.get('Defense', 0)
        speed=base.get('Speed', 0)


        print(f"Name: {name}")
        print(f"Type: {types}")
        print(f"Attack: {attack}")
        print(f"Defense: {defense}")
        print(f"Speed: {speed}")


def main():
    file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Pokemon\pokemons.json'
    pokemons=load_pok(file_path)
    show_pok_info(pokemons)


if __name__ == '__main__':
    main()




