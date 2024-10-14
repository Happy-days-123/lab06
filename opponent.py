"""A class for an Opponent."""
from dataclasses import dataclass
from sprite import Sprite
from typing_extensions import Self
from food import Food, FoodList
from character import Character
@dataclass
class Opponent(Sprite):
    """A competing player.Does everthing the same as player expect it eats food randomly """
    x: float
    y: float
    size: float
    speed: float
    color: str
    count: int = 0
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
    def move(self, food_list: FoodList) -> Self:
        closest: Food | None = None
        for f in food_list.food:
            if closest is None:
                closest = f
            if f.distance(self) < closest.distance(self):
                closest = f
        direction = self.direction(closest)
        self.x = self.x + (self.speed * direction[0])
        self.y = self.y + (self.speed * direction[1])
        return self
            
    