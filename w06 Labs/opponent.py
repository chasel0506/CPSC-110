"""A class for an Opponent."""
from dataclasses import dataclass
from character import Character
from typing_extensions import Self
from food import Food, FoodList
import random
@dataclass
class Opponent(Character):
    """A competing player."""    
    # TODO: Write an opponent class that extends Sprite.

    def move(self, food_list: FoodList) -> Self:
        closest: Food | None = None
        min_distance = float('inf')  # Start with infinity

        for f in food_list.food:
            distance_to_food = f.distance(self)
            if distance_to_food < min_distance:
                min_distance = distance_to_food
                closest = f
            elif distance_to_food == min_distance:
            # Randomly choose between two equidistant food items
                if random.choice([True, False]):
                    closest = f

        if closest:  # Check if closest food is not None
            direction = self.direction(closest)
            self.x += self.speed * direction[0]
            self.y += self.speed * direction[1]
        return self
