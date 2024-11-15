"""Manages Food state."""
import math
from typing import List
from dataclasses import dataclass
from player import Player
import random

@dataclass
class Food:
    """Manages Food state."""
    x: float
    y: float
    size: float = 10

    def move(self):
        """Move food randomly in the x and y directions."""
        self.x += random.uniform(-5, 5)  
        self.y += random.uniform(-5, 5)  

    def hit(self, player: Player) -> bool:
        """Check if the food is touching the player."""
        distance = ((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5
        return distance < (self.size + player.size)  # Check if they overlap

@dataclass
class FoodList:
    """Manages a list of Food objects."""
    food: List[Food]

    def populate(self, count: int, screen_width: int, screen_height: int):
        """Populate the food list with Food objects at random positions."""
        self.food = []
        for _ in range(count):
            x = random.uniform(0, screen_width)
            y = random.uniform(0, screen_height)
            self.food.append(Food(x, y))  # Default size of 10 for food

    def move_all(self):
        """Move all food items in the list."""
        for food in self.food:
            food.move()

    def remove_food(self, food_item: Food):
        """Remove a specific food item from the list."""
        self.food.remove(food_item)
