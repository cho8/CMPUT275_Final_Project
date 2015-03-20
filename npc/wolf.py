import pygame, npc
from npc import BaseNPC
from tiles import Tile

class Wolf(BaseNPC):
    """
    Predator NPC class.
    
    Modes: Fight, Flight, Neutral
    
    """
    sprite = pygame.image.load("images/wolf.png")

    def __init__(self, **keywords):
        self._base_image = Wolf.sprite
        
        # Set base class
        super().__init__(**keywords)

        self.health = 10
        self.speed = 10
        self.atk = 5
        self.type = "Wolf"

npc.active_npcs["Wolf"] = Wolf


