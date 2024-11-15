"""Example game showing a circle moving on screen."""
import pygame

from game import Game
from player import Player
from food import FoodList
from opponent import Opponent
from keys import pressed_keys, directions

# TODO: Refactor draw to act on list of Sprite and draw all Sprites
def draw(game: Game, player: Player, opponent: Opponent, food_list: FoodList):
    game.screen.fill(game.background)
    """
    Draws the player and game on the screen.
    
    Note that because this function has only side-effects, it would take a
    simulation to test. We can do that, but for this class, it's a bit much.
    Therefore, we don't have any tests for this.
    """
    game.screen.fill(game.background)
    
    #opponent
    pygame.draw.circle(
        game.screen,
        opponent.color,  
        pygame.Vector2(opponent.x, opponent.y),
        opponent.size
    )
    
    #player
    pygame.draw.circle(
        game.screen,
        player.color,  
        pygame.Vector2(player.x, player.y),
        player.size
    )

    for f in food_list.food:
        pygame.draw.circle(
            game.screen,
            "green",
            pygame.Vector2(f.x, f.y),
            f.size
        )
    pygame.display.flip()
    
def main():
    # Define the Game state
    game = Game(
        screen     = pygame.display.set_mode((1280, 720)),
        clock      = pygame.time.Clock(),
        background = "white",
        fps        = 120,
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
              color = "Light Blue"
    )

    # Initialize pygame
    pygame.init()

    food_list = FoodList([])
    food_list.populate(100, (game.screen.get_width(), game.screen.get_height()))

    # Define the opponent after initializing food_list
    opponent = Opponent(
              x     = 1500,
              y     = 1000,
              size  = 10,
              speed = 10,
              color = "red"
    )

    # Run forever in a loop until quit
    while game.running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()

        # Move the game clock forward
        game.tick()

        # Move the opponent
        opponent.move(food_list)

        # Get pressed keys and directions
        pressed = pressed_keys(pygame.key.get_pressed())
        dirs = directions(game.keymap, pressed)

        # Move the player
        player.move(game.deltaT, dirs)

        if pygame.mouse.get_focused():
            player.move_to(pygame.mouse.get_pos())
        
        food_list.eat(player)
        food_list.eat(opponent)
        food_list.move()

        # Draw the game
        draw(game, player, opponent, food_list)

# Run the main function
if __name__ == "__main__":
    main()
