"""A super-class for anything onscreen that moves."""
import math
from typing import Tuple 
from typing_extensions import Self
from dataclasses import dataclass
@dataclass
class Sprite:
    """A class for anything that is drawn on screen."""
    x: int
    y: int
    size: int
    
    def move(self, dx: int, dy: int) -> Self:
        """
        Purpose: Moves the food by a given amount (dx, dy) in the x and y directions.
        This simulates food drifting or moving slightly within the game world.
        
        Examples:
            f = Food(x=100, y=100, size=10)
            move(f, 5, -5) -> Food(105, 95, 10)
            move(f, -10, 10) -> Food(95, 105, 10)
        """
        self.x += dx
        self.y += dy
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
    
    
    
    def direction(self, other: Self) -> Tuple[int, int]:
        # Step 1: Subtract the x and y coordinates of the two sprites to get the vector
        vector: Tuple[int, int] = (other.x - self.x, other.y - self.y)
        
        # Step 2: Compute the magnitude of the vector (ensure it's an int, so we can use floor later)
        magnitude: float = math.sqrt(vector[0]**2 + vector[1]**2)
        
        # Step 3: Normalize the vector (avoid division by zero)
        if magnitude == 0:
            return (0, 0)  # Return a zero vector if magnitude is zero
        
        # Step 4: Normalize and use floor to ensure the result is integer
        normalized_vector: Tuple[int, int] = (
            math.floor(vector[0] / magnitude), 
            math.floor(vector[1] / magnitude)
        )
        
        return normalized_vector
    