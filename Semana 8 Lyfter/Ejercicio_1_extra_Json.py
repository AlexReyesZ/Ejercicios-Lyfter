import json

file_path=r'C:\Users\LightForceCR\Desktop\Programacion\week_8\Pokemon\pokemons.json'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemons_info=json.load(file)
except FileNotFoundError:
    print('File not found. Check the path')
    pokemon_info=[]

print('\n   Pokemon list    ')

for pokemon in pokemons_info:
    pok_name= pokemon['name']['english']
    pok_types=','.join(pokemon['type'])
    pok_hp=pokemon['base']['HP']
    pok_attack=pokemon['base']['Attack']
    pok_defense=pokemon['base']['Defense']
    pok_sp_attack = pokemon['base'].get('Sp. Attack', pokemon['base'].get('Sp_attack', 0))
    pok_sp_defense = pokemon['base'].get('Sp. Defense', pokemon['base'].get('Sp_defense', 0))
    pok_speed=pokemon['base']['Speed']

    print(f'Name: {pok_name} | Type:{pok_types} | HP: {pok_hp} \
    | Attack: {pok_attack} | Defense: {pok_defense} | Sp. Attack: {pok_sp_attack} \
    | Sp. Defense: {pok_sp_defense} | Speed: {pok_speed}')