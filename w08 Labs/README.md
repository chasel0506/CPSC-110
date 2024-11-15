CPSC 110 Lab 8 Due: Fri Nov. 1, 2024, 9:00am

General Lab Instructions:
1. All assignments will be submitted through Canvas. If you submit multiple times, the most recent submission will be graded.

2. You will typically explain your code from the last lab to the instructor at the beginning of the next lab to receive your full marks and feedback.

3. If you work with other people, list all of your names on the assignment. Each assignment will specify how many others you can work with.

4. Please review the collage’s plagiarism policies. As a general rule, copy/paste should never be used for any code. Ever. You may discuss topics with other students and reference online materials, but the final assignment must be written by the student. If you reference materials/people besides the textbook/instructor then cite this in a file contributions.txt. Full citations are not necessary, a bullet point list of the materials/people that you references is suitable.

5. Code will be graded for functionality as well as quality. This means code that should be easy to read with descriptive variable names and appropriate comments.

6. You should aim to stick to the concepts we have already covered in class. For example, do not use ”if statements” on assignment 1 since it was not covered in lecture 1. If you have studied programming elsewhere then it is tempting to jump ahead, but full marks will only be given to assignments that are focused on this course’s content.

7. Code that cannot run successively in Python 3 will receive a zero. Make sure you are using the correct python version and allow yourself enough time for thorough testing.

8. At the start of each assignment will be a list of the required files for submission. All files should be com- pressed in one zip folder named <studentnumber>_<yourname >_LAB < number >_CPSC110.zip. For example: 21870110_LUKESKYWALKER_LAB01_CPSC110.zip

See below for Required files.

# Lab 08: File I/O
This week's lab has two parts:
- Individual (or pairs) component where you parse GTFS data
- Group component where you create your own CSV data reader and writer

## Individual Component
You will need to recreate a version of the provided `stop_parser.py` for `routes.txt`, i.e., create `routes_parser.py`. Namely, you'll need to create:
- A high-level data model of the CSV (i.e., `class Route`).
- Validated sub-types that align with GTFS specifications for each `Route` attribute
- Command functions that call helper functions to parse
- A test suite that mirrors `stop_parser_tests.py`

Although there is a lot of typing that needs to be done, most of the logic has been worked out for you in `stop_parser.py`. You may copy, reuse, and import the code from `stop_parser.py`, but you need to appropriately rename and document any functions you use.

## Group component
You'll remember from last week that maintaining game state will be one person's responsibility. Although it is their job to CODE the game state, everyone will be responsible for DESIGNING the game state.

Using the GTFS model, create a specification for your game state. It's OK if it changes over time, but the specification must be complete, testable, and runnable. For example, you might specify `food.csv` like the following:

### food.csv
#### File: required
##### Primary key (food_id)
| Field Name | Type       | Presence | Description |
| ---------- | ---------- | -------- | ----------- |
| food_id    | Unique ID  | Required | A unique ID for every food item.  |
| x          | Screen X | Required | The x-position of the food on screen. |
| y          | Screen Y | Required | The y-position of the food on screen. |
| visible    | Boolean    | Optional | Whether the food can be seen. | 

#### Field types:
- **Unique ID**: An ID field value is an internal ID, not intended to be shown to riders, and is a sequence of any UTF-8 characters. Using only printable ASCII characters is recommended. An ID is labeled "unique ID" when it must be unique within a file. IDs defined in one .txt file are often referenced in another .txt file. IDs that reference an ID in another table are labeled "foreign ID".
- **Screen X**: an integer between 0 and Screen Width
- **Screen Y**: an integer between 0 and Screen Height
- **Screen Width**: an integer that describes the width of the screen
- **Screen Height**: an integer that describes the height of the screen

### Group Tasks
- Fully specify your game state
- Write a stub CSV writer and parser for each class
- Add the writers and parser to your overall UML diagram
- Determine which coders will depend on game state and write stubs for loading and saving game state

### State management team member:
One person will be responsibile for this portion of the project. Their job will be to maintain the code for reading and writing game state. Determine who that is. You do NOT have to finish this portion of the code for next week, but you DO have to maintain your code so that the rest of the project doesn't break. Note that you may have additional tasks as the project continues.
