CPSC 110 Lab 2 Due: Fri Sept. 20, 2024, 9:00am

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
- Due: Fri Sep. 27, 2023, 9:00am
- Required files:
  - hello.py
  - table.md
  - pokemon.py
  - pokemon_api.py
  - .gitignore
  - README.md



# Lab 03 HtDF

Download the full code at `https://github.com/CC-CPSC-110/lab03/` by using your GitHub Desktop app.

For each problem, write the signature, purpose, and stub. 

### Problem 1:
    
Design a function that accepts a string and returns the string with 'Hello world! ' at the beginning of the string.

For example, if you call the function with "Good Morning", the function should return "Hello world! Good Morning".

When designing your function, be sure to follow all steps of the HtDF recipe.

### Problem 1:
    
Design a function that accepts a string and returns the string with 'Hello world! ' at the beginning of the string.

For example, if you call the function with "Good Morning", the function should return "Hello world! Good Morning".

When designing your function, be sure to follow all steps of the HtDF recipe.


### Problem 2:

We are working with an API: https://pokeapi.co/. This API allows us to fetch different types (e.g., name, type, height, weight, base_stat) of information on Pokemon.

Here are some functions of interest:

- `get_pokemon_name(pokemon_id: int) -> str`


- `get_pokemon_attack(pokemon_name: str) -> int`


- `get_pokemon_defense(pokemon_name: str) -> int`


- `get_pokemon_height(pokemon_name: str) -> int`


- `get_pokemon_weight(pokemon_name: str) -> int`


- `get_pokemon_num_types(pokemon_name: str) -> int`


- `get_pokemon_type1(country_name: str) -> str`


- `get_pokemon_type2(country_name: str) -> str`


Complete the following table as a [markdown](https://www.markdownguide.org/) file with information about three different Pokemon. Each Pokemon has a unique ID number. If you are not familiar with Pokemon, just choose three random numbers from 1 to 898 (inclusive).

The first row is provided as an example and does not count towards the three rows you have to fill out yourself.


| ID  | Name       | Attack | Defense | Number of Types | Type 1  | Type 2  |
| --- | ---        | ---    | ---     | ---             | ---     | ---     |
| 132 | ditto      | 48     | 48      | 1               | normal  | None    |


# Example of how the first row was completed.

```python
get_pokemon_name(132)
get_pokemon_attack("ditto")
get_pokemon_defense("ditto")
get_pokemon_num_types("ditto")
get_pokemon_type1("ditto")
get_pokemon_type2("ditto")
```

### Problem 3:

As indicated by the table in Problem 2, Pokemon have a given type and on occasion, a secondary type. Every Pokemon also has an associated attack value.

In this problem, we will work with something called a modified attack value. The modified attack value is the attack value of a Pokemon multiplied by the number of types that it has.

Design a function that accepts a Pokemon ID number and returns the modified attack value.

When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**.

### Problem 4:

Given two Pokemons IDs, design a function that returns the name of the Pokemon with the largest modified attack. If possible, try to call your function from Problem 3.
    
When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**. 

### Problem 5:

In one-on-one battle, an attacking Pokemon inflicts damage if its modified attack is strictly greater than the other Pokemon's defense.  Given the ID of the attacking Pokemon and the ID of the defending Pokemon, design a function to determine if the attacking Pokemon inflicts damage. 

For this problem, you should consider the attack of a Pokemon as its modified attack as calculated in Problem 3.
    
When designing your function, be sure to follow all steps of the HtDF recipe **including designing your tests first**.
