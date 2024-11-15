"""Test suite for game."""
import pygame
from cs110 import expect, summarize
import game
import player
import keys
from food import *

#------------------------------------------------------------------------------#
# Setup: Run these before all tests.
#------------------------------------------------------------------------------#
test_game = game.Game(
        screen     = pygame.display.set_mode((1280, 720)),
        clock      = pygame.time.Clock(),
        background = "purple",
        fps        = 60,
        running    = True,
        deltaT     = 0,
        keymap     = {
                        "w": "UP",
                        "s": "DOWN",
                        "a": "LEFT",
                        "d": "RIGHT"
        },
    )

test_player_1 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_2 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_3 = player.Player(x=100, y=100, size=10, speed=10, color="red")
test_player_4 = player.Player(x=100, y=100, size=10, speed=10, color="red")

test_player_UP = player.Player(x=100, y=  0, size=10, speed=10, color="red")
test_player_DN = player.Player(x=100, y=200, size=10, speed=10, color="red")
test_player_LT = player.Player(x=200, y=100, size=10, speed=10, color="red")
test_player_RT = player.Player(x=  0, y=100, size=10, speed=10, color="red")


#------------------------------------------------------------------------------#
# Test player.move
#------------------------------------------------------------------------------#
expect(test_player_1.move(10, ["UP"]),    test_player_UP)
expect(test_player_2.move(10, ["DOWN"]),  test_player_DN)
expect(test_player_3.move(10, ["RIGHT"]), test_player_LT)
expect(test_player_4.move(10, ["LEFT"]),  test_player_RT)


#------------------------------------------------------------------------------#
# Test player.directions
#------------------------------------------------------------------------------#
expect(keys.directions(test_game.keymap, ["w"]),      ["UP"])
expect(keys.directions(test_game.keymap, ["s"]),      ["DOWN"])
expect(keys.directions(test_game.keymap, ["a"]),      ["LEFT"])
expect(keys.directions(test_game.keymap, ["d"]),      ["RIGHT"])
expect(keys.directions(test_game.keymap, ["w", "a"]), ["UP", "LEFT"])
expect(keys.directions(test_game.keymap, ["w", "d"]), ["UP", "RIGHT"])
expect(keys.directions(test_game.keymap, ["s", "a"]), ["DOWN", "LEFT"])
expect(keys.directions(test_game.keymap, ["s", "d"]), ["DOWN", "RIGHT"])


#------------------------------------------------------------------------------#
# Test keys.pressed_keys
#------------------------------------------------------------------------------#
expect(keys.pressed_keys((False,) * 8   + (True,) * 2), ['backspace', 'tab'])
expect(keys.pressed_keys((False,) * 97  + (True,) * 3), ['a', 'b', 'c'])
expect(keys.pressed_keys((False,) * 100 + (True,) * 1), ['d'])


#------------------------------------------------------------------------------#
# Test game.tick
#------------------------------------------------------------------------------#
expect(test_game.tick(), test_game)


# TODO: add tests for moving one Food (O)
# TODO: add tests for populating FoodList (O)
# TODO: add tests for moving the player with the mouse (O)
# TODO: add tests for hitting Food (O)
# TODO: add tests for consuming Food in the Player (O)
# TODO: add tests for removing a food from FoodList (O)
# TODO: add tests for changing the size of Player based on food count (O)

#------------------------------------------------------------------------------#
# Test food #test_17
#------------------------------------------------------------------------------#
test_food = Food(x=100, y=100, size=20)  # Initial position

# Move the food and expect it to change position
test_food.move()  # Move the food


#------------------------------------------------------------------------------#
# Test populating FoodList #test_18 ~ #test_28
#------------------------------------------------------------------------------#
test_food_list = FoodList(food=[])

# Populate the food list with 5 items
test_food_list.populate(count=5, screen_width=1280, screen_height=720)

# Expect the food list to have 5 items
expect(len(test_food_list.food), 5)

# Check that all food items are within the screen dimensions
for food_item in test_food_list.food:
    expect(0 <= food_item.x <= 1280, True)
    expect(0 <= food_item.y <= 720, True)
    
    
#------------------------------------------------------------------------------#
# Test moving the player with the mouse #test_29 #test_30
#------------------------------------------------------------------------------#
test_player_mouse = player.Player(x=0, y=0, size=10, speed=10, color="red")

# Move the player to mouse position (100, 200)
test_player_mouse.move_to_mouse(100, 200)

# Expect the player's position to be updated to the mouse position
expect(test_player_mouse.x, 100)
expect(test_player_mouse.y, 200)


#------------------------------------------------------------------------------#
# Test hitting Food #test_31 #test_32
#------------------------------------------------------------------------------#
test_player_hit = player.Player(x=100, y=100, size=20, speed=10, color="blue")
test_food_hit = Food(x=105, y=105, size=5)
# Check if the player hits the food

expect(test_food_hit.hit(test_player_hit), True)
# Check if no hit happens

test_food_hit_far = Food(x=500, y=500, size=5)
expect(test_food_hit_far.hit(test_player_hit), False)


#------------------------------------------------------------------------------#
# Test consuming Food in the Player #test_33
#------------------------------------------------------------------------------#
test_player_consume = player.Player(x=100, y=100, size=20, speed=10, color="green")
test_food_consume = Food(x=105, y=105, size=5)

# Initially, player should have no food consumed
test_player_consume.food_count = 0

# Simulate food consumption
if test_food_consume.hit(test_player_consume):
    test_player_consume.increment_food_count()

# Check if the player's food count has increased
expect(test_player_consume.food_count, 1)


#------------------------------------------------------------------------------#
# Test removing a food from FoodList #test_34 #test_35
#------------------------------------------------------------------------------#
test_food_list_remove = FoodList(food=[])
test_food_list_remove.populate(count=5, screen_width=1280, screen_height=720)

# Store the first food item
food_to_remove = test_food_list_remove.food[0]

# Remove the food item
test_food_list_remove.remove_food(food_to_remove)

# Expect the list to have one less item
expect(len(test_food_list_remove.food), 4)

# Ensure the removed item is no longer in the list
expect(food_to_remove not in test_food_list_remove.food, True)


#------------------------------------------------------------------------------#
# Test changing the size of Player based on food count #test_36 #test_37
#------------------------------------------------------------------------------#
test_player_size = player.Player(x=100, y=100, size=20, speed=10, color="orange")
test_player_size.food_count = 0

# Increment the food count and update size
test_player_size.increment_food_count()

# Expect the player's size to increase based on food count
# size = 10 + food_count * 0.5
expect(test_player_size.size, 10.5)  # Should increase as food_count is now 1

# Increment food count again and check size
test_player_size.increment_food_count()
expect(test_player_size.size, 11) 


#------------------------------------------------------------------------------#
# Summarize the tests
#------------------------------------------------------------------------------#
summarize()