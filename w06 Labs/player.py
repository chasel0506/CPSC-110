"""Manages Player state."""
import sys
from typing import List, Tuple
from sprite import Sprite
from character import Character
from dataclasses import dataclass

# Get the Python version as a tuple
python_version = sys.version_info

if python_version >= (3, 11):
    # Import for Python 3.11 and above
    from typing import Self
else:
    # Import for Python versions below 3.11
    from typing_extensions import Self

@dataclass
class Player(Character):
    """Describes the player."""
    # TODO: refactor to extend Character
    
    def move(self, deltaT: float, dirs: List[str]) -> Self:
        """
        Purpose: Moves a player by speed per change in time in given directions.
        Examples:
            player = Player(x=100, y=100, size=10, speed=10, color="red")
            move(player, 10, ["UP"])    -> Player(100,   0, 10, 10, "red")
            move(player, 10, ["DOWN"])  -> Player(100, 200, 10, 10, "red")
            move(player, 10, ["RIGHT"]) -> Player(200, 100, 10, 10, "red")
            move(player, 10, ["LEFT"])  -> Player(  0, 100, 10, 10, "red")
        """
        amount = self.speed * deltaT
        # we index from the top left so negative-y direction is up
        if "UP" in dirs:
            self.y -= amount 
        if "DOWN" in dirs:
            self.y += amount
        if "LEFT" in dirs:
            self.x -= amount
        if "RIGHT" in dirs:
            self.x += amount
        return self

    def move_to(self, mouse: Tuple[int, int]) -> Self:
        """
        Purpose: Moves the player directly to the given mouse coordinates (x, y).
        This simulates the player moving to the position of a mouse click or cursor location.
        
        Examples:
            player = Player(x=100, y=100, size=10, speed=10, color="red")
            move_to(player, (150, 200)) -> Player(150, 200, 10, 10, "red")
            move_to(player, (0, 0))     -> Player(0, 0, 10, 10, "red")
        """
        self.x = mouse[0]
        self.y = mouse[1]
        return self
