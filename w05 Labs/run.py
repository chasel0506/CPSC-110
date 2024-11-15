"""Example game showing a circle moving on screen."""
import pygame
from cs110 import expect, summarize
from game import Game
from player import *
from keys import pressed_keys, directions
from food import FoodList  

# Initialize FoodList
food_list = FoodList(food=[])
    
# TODO: draw your List of Food
def draw(game: Game, player: Player, food_list: FoodList):
    """
    Draws the player and game on the screen.
    
    Note that because this function has only side-effects, it would take a
    simulation to test. We can do that, but for this class, it's a bit much.
    Therefore, we don't have any tests for this.
    """
    game.screen.fill(game.background)
    pygame.draw.circle(
        game.screen,
        player.color,
        pygame.Vector2(player.x, player.y),
        player.size
    )
    # Draw each food item
    for food in food_list.food:
        pygame.draw.circle(
            game.screen,
            "green",  # Color of food
            (int(food.x), int(food.y)),
            food.size
        )
    pygame.display.flip()
    

def main():
    """
    Run the main game loop.
    
    Note: again, because this is a function that only has side effects, there's
    not really a clean way to test this. Main loops usually follow a command
    pattern like this where they coordinate functions from different files.
    """
    
    # Define the Game state
    game = Game(
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
                        "d": "RIGHT",
        },
    )

    # Define the player
    player = Player(
              x     = game.screen.get_width() / 2,
              y     = game.screen.get_height() / 2,
              size  = 10,
              speed = 300,
              color = "red"
              # TODO: add food count
    )
    
    # Initialze pygame
    pygame.init()

    # TODO: initialize FoodList
    food_list.populate(count=1000, screen_width=game.screen.get_width(), screen_height=game.screen.get_height())

    # Run forever in a loop until quit
    while game.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()

        # Move the game clock forward
        game.tick()

        # Get pressed keys and directions
        pressed = pressed_keys(pygame.key.get_pressed())
        dirs = directions(game.keymap, pressed)
        
        # Move the player
        player.move(game.deltaT, dirs)
        
        # TODO: move player depending on mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()  
        player.move_to_mouse(mouse_x, mouse_y)  
        
        # TODO: determine whether your Food has been consumed
        # TODO: run all actions depending on whether Food has been consumed
        # TODO: move the Food
        # TODO: draw the Food
        for food in food_list.food[:]:  
            if food.hit(player):  # Check if the player has consumed the food
                food_list.remove_food(food)  # Remove the food item if consumed
                player.increment_food_count()
        # TODO: extend to draw Food
        food_list.move_all()
        draw(game, player, food_list)


# Run the main function
if __name__ == "__main__":
    main()
