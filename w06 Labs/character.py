"""A super-class for anything that is trying to win."""
import math
from typing import Tuple 
from typing_extensions import Self
from dataclasses import dataclass
from sprite import Sprite

@dataclass
class Character(Sprite):
    """A class for competing entities."""
    # TODO: refactor Player and Opponent to extend Character
    speed: int
    color: str
    count: int = 0
        
    def move(self, delta_t: float, direction: Tuple[int, int]) -> Self:
        self.x += self.speed * direction[0] * delta_t
        self.y += self.speed * direction[1] * delta_t
        return self
    
    def eat(self) -> None:
        """
        Purpose: Increases the player's food consumption count by 1. This method
        tracks how many pieces of food the player has eaten.
        
        Examples:
            player = Player(x=100, y=100, size=10, speed=10, color="red", count=0)
            eat(player) -> Player with count = 1
            eat(player) -> Player with count = 2
        """
        self.count += 1


    def resize(self) -> None:
        """
        Purpose: Resizes the player based on the amount of food consumed. The player's size
        is determined as 10 units plus the number of food items consumed (count).
        
        Examples:
            player = Player(x=100, y=100, size=10, speed=10, color="red", count=5)
            resize(player) -> Player with size = 15
            
            player = Player(x=100, y=100, size=10, speed=10, color="red", count=0)
            resize(player) -> Player with size = 10
        """
        self.size = 10 + self.count
