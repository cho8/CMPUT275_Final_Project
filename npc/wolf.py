import pygame, npc
from npc.base_npc import BaseNPC

class Wolf(BaseNPC):
    """
    Predator NPC class.
    
    Modes: Fight, Flight, Neutral
    
    """

    def __init__(self, **keywords):
        
        # Set base class
        super().__init__(**keywords)
        self.image = pygame.image.load("images/wolf.png").convert_alpha()
        self.image2 = pygame.image.load("images/wolf2.png").convert_alpha()
        self.front = self.image.subsurface(0,28,10,14)
        self.back = self.image.subsurface(10,28,10,14)
        self.left1= self.image.subsurface(0,0,29,14)
        self.right1 = self.image.subsurface(0,14,29,14)
        self.left2= self.image2.subsurface(0,0,29,14)
        self.right2 = self.image2.subsurface(0,14,29,14)
        self.image = self.left1
        self.rect = self.image.get_rect() 
        self.health = 10
        self.speed = 5
        self.atk = 5
        self.type = "Wolf"
 

npc.active_npcs["Wolf"] = Wolf


