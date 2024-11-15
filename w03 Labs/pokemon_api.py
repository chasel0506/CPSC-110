import requests

def get_pokemon_name(pokemon_id: int) -> str:
    """
    Returns a pokemon's name, according to https://pokeapi.co/.
    
    If pokemon_id is not in range [0, 898], returns an error message.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return as_json["name"]
    elif result.status_code == requests.codes.NOT_FOUND:
        return "Error. Please double check the Pokemon ID"
    else:
        return "Error. Unable to fetch results from website."


def get_pokemon_attack(pokemon_name: str) -> int:
    """
    Returns a pokemon's base stats, according to https://pokeapi.co/.
    
    If pokemon_name is not found returns -1.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return as_json["stats"][1]["base_stat"]
    elif result.status_code == requests.codes.NOT_FOUND:
        return -1
    else:
        return -1


def get_pokemon_defense(pokemon_name: str) -> int:
    """
    Returns a pokemon's base stats, according to https://pokeapi.co/.
    
    If pokemon_name is not found returns -1.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return as_json["stats"][2]["base_stat"]
    elif result.status_code == requests.codes.NOT_FOUND:
        return -1
    else:
        return -1
    

def get_pokemon_height(pokemon_name: str) -> int:
    """
    Returns a pokemon's height, according to https://pokeapi.co/.
    
    If pokemon_name is not found returns -1.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return as_json["height"]
    elif result.status_code == requests.codes.NOT_FOUND:
        return -1
    else:
        return -1


def get_pokemon_weight(pokemon_name: str) -> int:
    """
    Returns a pokemon's weight, according to https://pokeapi.co/.
    
    If pokemon_name is not found returns -1.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return as_json["weight"]
    elif result.status_code == requests.codes.NOT_FOUND:
        return -1
    else:
        return -1
  
def get_pokemon_num_types(pokemon_name: str) -> int:
    """
    Returns a pokemon's number of types, according to https://pokeapi.co/.
    
    If pokemon_name is not found, returns -1.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return len(as_json["types"])
    elif result.status_code == requests.codes.NOT_FOUND:
        return -1
    else:
        return -1

    
def get_pokemon_type1(pokemon_name: str) -> str:
    """
    Returns a pokemon's type 1, according to https://pokeapi.co/.
    
    If pokemon_name is not found, returns an error message.
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        return as_json["types"][0]["type"]["name"]
    elif result.status_code == requests.codes.NOT_FOUND:
        return "Error. There is no pokemon with the given name."
    else:
        return "Error. Unable to fetch results from website."
    
    
def get_pokemon_type2(pokemon_name: str) -> str:
    """
    Returns a pokemon's type 2, according to https://pokeapi.co/.
    
    If pokemon_name is not found, returns an error message.
    
    If pokemon_name does not have a second type, then returns "None".
    """
    result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if result.status_code == requests.codes.ok:
        as_json = result.json()
        if len(as_json["types"]) > 1:
            return as_json["types"][1]["type"]["name"]
        else:
            return "None"
    elif result.status_code == requests.codes.NOT_FOUND:
        return "Error. There is no pokemon with the given name."
    else:
        return "Error. Unable to fetch results from website."
