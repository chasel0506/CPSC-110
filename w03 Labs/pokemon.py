# Answer Problems 3, 5, and 5 here

# Problem #2
from pokemon_api import *
from cs110 import expect, summarize

def print_pokemon_info(pokemon_ids:int) -> int:
    # Title
    print("| ID  | Name       | Attack | Defense |  Types  | Type 1   | Type 2   |")
    print("|-----|------------|--------|---------|---------|----------|----------|")
    
    # Create a loop 
    for pokemon_id in pokemon_ids:
        name = get_pokemon_name(pokemon_id)
        attack = get_pokemon_attack(name)
        defense = get_pokemon_defense(name)
        types = get_pokemon_num_types(name)
        type1 = get_pokemon_type1(name)
        type2 = get_pokemon_type2(name)
                
        # Output (set line spacing)
        print(f"| {pokemon_id:<3} | {name:<10} | {attack:<6} | {defense:<7} | {types:<7} | {type1:<8} | {type2:<8} |")

# IDs of interest
pokemon_ids = [132, 311, 312, 898]
print_pokemon_info(pokemon_ids)
print()

# Problem 3 : Calculate Modified Attack Value
def calculate_modified_attack(pokemon_id: int) -> int:
    name = get_pokemon_name(pokemon_id)
    return get_pokemon_attack(name) * get_pokemon_num_types(name)

# Problem 4 : Compare Modified Attacks of Two Pokemons
def largest_attack(id1: int, id2: int) -> str:
    return get_pokemon_name(id1) if calculate_modified_attack(id1) >= calculate_modified_attack(id2) else get_pokemon_name(id2)

# Problem 5 : Determine Damage Inflicted in Battle
def inflict_damage(attacker_id: int, defender_id: int) -> bool:
    modified_attack = calculate_modified_attack(attacker_id)
    defender_name = get_pokemon_name(defender_id)
    defender_defense = get_pokemon_defense(defender_name)
    return modified_attack > defender_defense


# Problem 3 : Test
expect(calculate_modified_attack(132), equals=48)  
expect(calculate_modified_attack(311), equals=50)  
expect(calculate_modified_attack(312), equals=40)  
expect(calculate_modified_attack(898), equals=160)
# Problem 4 : Test
expect(largest_attack(123, 234), equals="scyther", description="The highest attack is [scyther]") 
expect(largest_attack(345, 456), equals="lileep", description="The highest attack is [lileep]")  
# Problem 5 : Test
expect(inflict_damage(123, 234), equals=True)  
expect(inflict_damage(345, 456), equals=True)
summarize()  # Summarize the test results
