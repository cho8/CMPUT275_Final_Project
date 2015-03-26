import pygame, npc
from npc.base_npc import BaseNPC
#from tiles import Tile

class Wolf(BaseNPC):
    """
    Predator NPC class.
    
    Modes: Fight, Flight, Neutral
    
    """

    def __init__(self, **keywords):
        
        # Set base class
        BaseNPC.__init__(self, **keywords)
        self.image = pygame.image.load("images/wolf.png").convert_alpha()
        self.rect = self.image.get_rect() 
        self.health = 10
        self.speed = 3
        self.atk = 5
        self.type = "Wolf"

npc.active_npcs["Wolf"] = Wolf


