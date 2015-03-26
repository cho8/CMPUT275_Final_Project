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
        self.front = self.image.subsurface(0,28,10,14)
        self.back = self.image.subsurface(10,28,10,14)
        self.left= self.image.subsurface(0,0,29,14)
        self.right = self.image.subsurface(0,14,29,14)
        self.image = self.front
        self.rect = self.image.get_rect() 
        self.health = 10
        self.speed = 1
        self.atk = 5
        self.type = "Wolf"
 

npc.active_npcs["Wolf"] = Wolf


