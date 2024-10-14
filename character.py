"""A super-class for anything that is trying to win."""
import math
from typing import Tuple 
from typing_extensions import Self
from dataclasses import dataclass


@dataclass
class Character():
    """A class for competing entities."""
    # TODO: refactor Player and Opponent to extend Character
    x: float
    y: float
    size: float
    speed: float
    color: str
    count: int = 0
    
    
    
        
   
        

    
   
    
    
    