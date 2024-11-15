"""A copy of your file from last week with the test cases removed."""
from pokemon_api import *
from dataclasses import dataclass
from typing import List
    


##3 : Calculate Modified Attack Value
def calculate_modified_attack(pokemon_id: int) -> int:
    name = get_pokemon_name(pokemon_id)
    attack = get_pokemon_attack(name)
    num_types = get_pokemon_num_types(name)
    
    modified_attack = attack * num_types
    return modified_attack

##4 : Compare Modified Attacks of Two Pokemons
def largest_attack(id1: int, id2: int) -> str:
    modified_attack1 = calculate_modified_attack(id1)
    modified_attack2 = calculate_modified_attack(id2)
    
    if modified_attack1 >= modified_attack2:
        return get_pokemon_name(id1).lower()
    else:
        return get_pokemon_name(id2).lower()

##5 : Determine Damage Inflicted in Battle
def inflict_damage(attacker_id: int, defender_id: int) -> bool:
    modified_attack = calculate_modified_attack(attacker_id)
    defender_name = get_pokemon_name(defender_id)
    defender_defense = get_pokemon_defense(get_pokemon_name(defender_id))
         
    if modified_attack > defender_defense:
        return True
    else:
        return False


