CPSC 110 Lab 4 Due: Fri Oct. 04, 2024, 9:00am

General Lab Instructions:
1. All assignments will be submitted through Canvas. If you submit multiple times, the most recent submission will be graded.

2. You will typically explain your code from the last lab to the instructor at the beginning of the next lab to receive your full marks and feedback.

3. If you work with other people, list all of your names on the assignment. Each assignment will specify how many others you can work with.

4. Please review the collage’s plagiarism policies. As a general rule, copy/paste should never be used for any code. Ever. You may discuss topics with other students and reference online materials, but the final assignment must be written by the student. If you reference materials/people besides the textbook/instructor then cite this in a file contributions.txt. Full citations are not necessary, a bullet point list of the materials/people that you references is suitable.

5. Code will be graded for functionality as well as quality. This means code that should be easy to read with descriptive variable names and appropriate comments.

6. You should aim to stick to the concepts we have already covered in class. For example, do not use ”if statements” on assignment 1 since it was not covered in lecture 1. If you have studied programming elsewhere then it is tempting to jump ahead, but full marks will only be given to assignments that are focused on this course’s content.

7. Code that cannot run successively in Python 3 will receive a zero. Make sure you are using the correct python version and allow yourself enough time for thorough testing.

8. At the start of each assignment will be a list of the required files for submission. All files should be com- pressed in one zip folder named <studentnumber>_<yourname >_LAB < number >_CPSC110.zip. For example: 21870110_LUKESKYWALKER_LAB01_CPSC110.zip

Lab 03 intructions:
- Total points: 30
- Due: Fri Oct. 04, 2024, 9:00am
- Required files:
  - pokemon.py
  - pokemon_database.py
  - pokemon_api.py
  - .gitignore
  - README.md



# Lab 04 How to Design Data

Download the full code at `https://github.com/CC-CPSC-110/lab04/` by using your GitHub Desktop app.

For each problem, write the signature, purpose, and stub. 

Add any required notes to `README.md` for citations, etc.

### Problem 1:

Again this week, we are working with an API: https://pokeapi.co/. This API allows us to fetch different types (e.g., name, type, height, weight, base_stat) of information on Pokemon.

Here are some functions of interest:

- `get_pokemon_name(pokemon_id: int) -> str`


- `get_pokemon_attack(pokemon_name: str) -> int`


- `get_pokemon_defense(pokemon_name: str) -> int`


- `get_pokemon_height(pokemon_name: str) -> int`


- `get_pokemon_weight(pokemon_name: str) -> int`


- `get_pokemon_num_types(pokemon_name: str) -> int`


- `get_pokemon_type1(country_name: str) -> str`


- `get_pokemon_type2(country_name: str) -> str`


Last week, we created a markdown file that had three pokemon in it. This week, we're going to create our own mirror of the pokemon database.

| ID  | Name       | Attack | Defense | Number of Types | Type 1  | Type 2  |
| --- | ---        | ---    | ---     | ---             | ---     | ---     |
| 132 | ditto      | 48     | 48      | 1               | normal  | None    |

Create a `class` called `Pokemon` in `pokemon_database.py` that stores each column of the table as an attribute of the class. Then, create a function called `populate_database` that takes a `List` of numbers and produces a database of pokemon.

Don't make the list too large, we don't want to hammer their servers and get blocked :) 

Remember the api calls from last week:

```python
get_pokemon_name(132)
get_pokemon_attack("ditto")
get_pokemon_defense("ditto")
get_pokemon_num_types("ditto")
get_pokemon_type1("ditto")
get_pokemon_type2("ditto")
```

Use them in your database creation function.

### Problem 2:
Copy your code from last lab into `pokemon.py` but remove the test cases (we're assuming you completed the test cases last week). Import your code as a module in `pokemon_database.py` so that you can use it in this lab. 

Write a function called `add_pokemon` that adds a pokemon to your database if and only if it doesn't already exist in the database. No duplicates are allowed. **Use the HtDF and HtDD formula, i.e., write test cases first.**

### Problem 3:

Just like last week, we're going to simulate pokemon attacks. However, this week, we're going to use our local database and update it only when needed.

As indicated by the table in Problem 2, Pokemon have a given type and on occasion, a secondary type. Every Pokemon also has an associated attack value.

In this problem, we will work with something called a modified attack value. The modified attack value is the attack value of a Pokemon multiplied by the number of types that it has.

Design a function that accepts a Pokemon ID number and returns the modified attack value. **However, today, write your function so that it updates and uses the local database** and use your `pokemon.py` module to check the correctness of your answers. For example, if you don't have the Pokemon ID in the database, your function needs to call `add_pokemon` first.

When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**.

### Problem 4
Given two Pokemons IDs, design a function that returns the name of the Pokemon with the largest modified attack. If possible, try to call your function from Problem 3.

**However, today, write your function so that it updates and uses the local database** and use your `pokemon.py` module to check the correctness of your answers. For example, if you don't have the Pokemon ID in the database, your function needs to call `add_pokemon` first.

When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**. 

### Problem 5:

In one-on-one battle, an attacking Pokemon inflicts damage if its modified attack is strictly greater than the other Pokemon's defense.  Given the ID of the attacking Pokemon and the ID of the defending Pokemon, design a function to determine if the attacking Pokemon inflicts damage. 

For this problem, you should consider the attack of a Pokemon as its modified attack as calculated in Problem 3.

**However, today, write your function so that it updates and uses the local database** and use your `pokemon.py` module to check the correctness of your answers. For example, if you don't have the Pokemon ID in the database, your function needs to call `add_pokemon` first.

When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**.

### Problem 6:
Now that we have a local database, we can start to store data that we care about. Modify your database so that a `Pokemon` includes `hit points` or `hp` to indicate the number of hitpoints that a Pokemon has. You can create any default amount of HP.

Write a function called `damage` that consumes a `Pokemon` and an amount of damage as an `int` and returns the `Pokemon` with the reduced `hp`.

When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**.

### Problem 7:
Now that we have a local database, we can start to store data that we care about. When a Pokemon is modified, we need to return it to the database and update the object.

Design a function called `update_database` that consumes a database and a `Pokemon` and returns the updated database. 

Your database needs to pass further tests for this problem. The database cannot contain duplicates, and no other Pokemon than the one you specified should be impacted. Design a robust test suite to ensure your database is correct.

When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**.

### Problem 8:
Now, finally, we can simulate a Pokemon attack. Creatively determine a way to demonstrate a Pokemon attack. If you need to write extra functions, use the HtDF recipe, including all tests. Be prepared to explain how your demonstration works.
