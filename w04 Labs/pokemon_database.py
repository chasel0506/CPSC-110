"""A file for your implementation of the local database."""
import pokemon
from pokemon import *
from pokemon_api import *
from dataclasses import dataclass
from typing import List
from cs110 import expect, summarize



@dataclass
class Pokemon:
    pokemon_id: int
    name: str
    attack: int
    defense: int
    types: int
    type1: str
    type2: str
    hp: int = 100  # Default HP value #[Problem6]

database = []
##[Problem 1]##
def populate_database(pokemon_ids: List[int]) -> List[Pokemon]:
    # Title
    print("| ID  | Name       | Attack | Defense |  Types  | Type 1   | Type 2   |")
    print("|-----|------------|--------|---------|---------|----------|----------|")
    # Create a loop to iterate each pokemon_id to fetch data from API
    for pokemon_id in pokemon_ids:
        name = get_pokemon_name(pokemon_id)
        attack = get_pokemon_attack(name)
        defense = get_pokemon_defense(name)
        types = get_pokemon_num_types(name)
        type1 = get_pokemon_type1(name)
        type2 = get_pokemon_type2(name)
                
        
        # Output (set line spacing)
        print(f"| {pokemon_id:<3} | {name:<10} | {attack:<6} | {defense:<7} | {types:<7} | {type1:<8} | {type2:<8} |")

        # Create a Pokemon object and add it to the database
        pokemon = Pokemon(pokemon_id, name, attack, defense, types, type1, type2)
        database.append(pokemon)
        
    return database

# IDs of interest
pokemon_ids = [132, 311, 312, 898]
database = populate_database(pokemon_ids)



##[Problem 2]##
def add_pokemon(database: list[Pokemon], new_pokemon_id: int) -> bool:
    for pokemon in database:
        if pokemon.pokemon_id == new_pokemon_id:  # if new Pokemon already exists in database
            return False  
    
    # If not found, fetch the details from the API
    name = get_pokemon_name(new_pokemon_id)
    attack = get_pokemon_attack(name)
    defense = get_pokemon_defense(name)
    types = get_pokemon_num_types(name)
    type1 = get_pokemon_type1(name)
    type2 = get_pokemon_type2(name)
    
    # Create a new Pokemon object
    new_pokemon = Pokemon(new_pokemon_id, name, attack, defense, types, type1, type2)
    
    # Add the new Pokemon to the database
    database.append(new_pokemon)
    return True  # Successfully added
        
expect(add_pokemon(database, 25), equals=True)           #test_01

# check if the new pokemon has been added successfully
if add_pokemon(database, 25): 
    print("Pokemon 25 added successfully!")
else:
    print("Pokemon 25 is already in the database.")



##[Problem 3]##
def get_modified_attack(pokemon_id: int) -> int:
    modified_attack: int
    
    for pokemon in database:
        if pokemon.pokemon_id == pokemon_id:
            modified_attack = calculate_modified_attack(pokemon_id)
            return modified_attack
        else:
            add_pokemon(database, pokemon_id)
            modified_attack = calculate_modified_attack(pokemon_id)
            return modified_attack
        
expect(get_modified_attack(132), equals=48)             #test_02
expect(get_modified_attack(311), equals=50)             #test_03
expect(get_modified_attack(312), equals=40)             #test_04
expect(get_modified_attack(898), equals=160)            #test_05
expect(get_modified_attack(25), equals=55)              #test_06
expect(get_modified_attack(51), equals=100)             #test_07



##[Problem 4]##
def get_largest_attack(id1: int, id2: int) -> str:
    # Ensure both Pokemon are in the database
    add_pokemon(database, id1)
    add_pokemon(database, id2)
    
    return largest_attack(id1, id2)

expect(get_largest_attack(25, 311), equals="pikachu")   #test_08
expect(get_largest_attack(132, 898), equals="calyrex")  #test_09
expect(get_largest_attack(1, 2), equals="ivysaur")      #test_10



##[Problem 5]##
def get_inflict_damage(attacker_id: int, defender_id: int) -> bool:
    # Ensure both Pokemon are in the database
    add_pokemon(database, attacker_id)
    add_pokemon(database, defender_id)

    return inflict_damage(attacker_id, defender_id)

expect(get_inflict_damage(123, 234), equals=True)       #test_11
expect(get_inflict_damage(456, 345), equals=False)      #test_12



##[Problem 6]##
def damage(pokemon: Pokemon, damage_amount: int) -> Pokemon:   
    # Calculate new HP
    new_hp = max(pokemon.hp - damage_amount, 0)  # Ensure HP doesn't go below 0
    
    # Create a new Pokemon object with updated HP
    updated_pokemon = Pokemon(
        pokemon.pokemon_id,
        pokemon.name,
        pokemon.attack,
        pokemon.defense,
        pokemon.types,
        pokemon.type1,
        pokemon.type2,
        new_hp
    )
    
    return updated_pokemon

def damage_tests():
    # Create a demo Pokemon
    demo = Pokemon(111111, "demo", 90, 55, 2, "electric", "None")  # By default hp = 100
    
    # Case 1: hp > damage
    updated_pokemon = damage(demo, 20)
    expect(updated_pokemon.hp, equals=80)               #test_13
    # Case 2: hp = damage
    updated_pokemon = damage(demo, 100)
    expect(updated_pokemon.hp, equals=0)                #test_14
    # Case 3: hp < damage
    updated_pokemon = damage(demo, 120)
    expect(updated_pokemon.hp, equals=0)                #test_15
    # reset demo with initial hp
    demo = Pokemon(111111, "demo", 90, 55, 2, "electric", "None")
    # Case 4: receive two damages in a row
    updated_pokemon = damage(demo, 20)
    updated_pokemon = damage(updated_pokemon, 30)
    expect(updated_pokemon.hp, equals=50)               #test_16

damage_tests()



##[Problem 7]##
def update_database(database: List[Pokemon], updated_pokemon: Pokemon) -> List[Pokemon]:
    # Look for Pokemon id in the database
    for pokemon in database:
        if pokemon.pokemon_id == updated_pokemon.pokemon_id:
            # id found, update the existing Pokemon
            pokemon.name = updated_pokemon.name
            pokemon.attack = updated_pokemon.attack
            pokemon.defense = updated_pokemon.defense
            pokemon.types = updated_pokemon.types
            pokemon.type1 = updated_pokemon.type1
            pokemon.type2 = updated_pokemon.type2
            pokemon.hp = updated_pokemon.hp
            return database
    
    # If not found, return the database unchanged
    return database

def update_database_tests():
    # update ditto with new values
    new_ditto = Pokemon(132, "ditto", 80, 40, 2, "electric", "fire", 200)
    
    # call the function to update the database
    updated_database = update_database(database, new_ditto)
    
    # retrieve the updated ditto from the updated database
    updated_ditto = None
    for pokemon in updated_database:
        if pokemon.pokemon_id == 132:
            updated_ditto = pokemon
    
    # Test using expect function
    expect(updated_ditto.attack, equals=80)             #test_17       
    expect(updated_ditto.defense, equals=40)            #test_18     
    expect(updated_ditto.types, equals=2)               #test_19       
    expect(updated_ditto.type1, equals="electric")      #test_20
    expect(updated_ditto.type2, equals="fire")          #test_21 
    expect(updated_ditto.hp, equals=200)                #test_22        

update_database_tests()



##[Problem 8]##
def attack(attacker: Pokemon, defender: Pokemon) -> int:
    # calculate damage (attacker's attack - defender's defense)
    damage = max(0, attacker.attack - defender.defense)
    
    # reduce defender's HP
    defender.hp = max(0, defender.hp - damage)
    
    print(f"{attacker.name} attacks {defender.name}")
    print(f"{attacker.name} causes {damage} damage.")
    print(f"{defender.name}'s HP remaining: {defender.hp}).")
    
    # check if the defender has fainted
    if defender.hp == 0:
        print(f"{defender.name} is defeated!")
    return damage
        
def attack_tests():
    # initialize two demo Pokemons
    pokemon1 = Pokemon(111111, "pokemon1", 90, 60, 2, "electric", "None")
    pokemon2 = Pokemon(222222, "pokemon2", 40, 30, 1, "normal", "None")
    expect(attack(pokemon1, pokemon2), equals=60)      #test_23

attack_tests()

summarize()  # Summarize the test results