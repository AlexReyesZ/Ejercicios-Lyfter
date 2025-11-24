import json

def load_pokemons(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("ERROR: File not found.")
        return []
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON format.")
        return []



def group_levels_by_type(pokemon_list):
    type_levels = {}

    for pokemon in pokemon_list:
        name = pokemon.get("name", {}).get("english", "Unknown")
        types = pokemon.get("type", [])
        base = pokemon.get("base", {})
        level = base.get("Speed", 0)  

        
        try:
            level = int(level)
        except ValueError:
            level = 0  

        for p_type in types:
            if p_type not in type_levels:
                type_levels[p_type] = []
            type_levels[p_type].append(level)

    return type_levels



def show_avg_levels(type_levels):
    print("\n--- Average Pokémon Level by Type ---")
    for p_type, levels in type_levels.items():
        if not levels:
            avg_level = 0
        else:
            avg_level = sum(levels) / len(levels)
        print(f"Type: {p_type} → Average Level: {avg_level:.2f}")




def main():
    file_path = r"C:\Users\LightForceCR\Desktop\Programacion\week_8\Pokemon\pokemons.json"
    pokemons = load_pokemons(file_path)

    type_levels = group_levels_by_type(pokemons)
    show_avg_levels(type_levels)

if __name__ == "__main__":
    main()