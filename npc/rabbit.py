import pygame, npc
from npc.base_npc import BaseNPC


class Rabbit(BaseNPC):
    """
    Prey NPC class.
    
    Modes Flight, Neutral
    """


    def __init__(self, **keywords):
        super().__init__(**keywords)
        self.image = pygame.image.load("images/rabbit.png").convert_alpha()
        self.image2 = pygame.image.load("images/rabbit_hop.png").convert_alpha()
        self.front1 = self.image.subsurface(0,12,5,6)
        self.back1 = self.image.subsurface(5,12,5,6)
        self.left1= self.image.subsurface(0,0,11,6)
        self.right1 = self.image2.subsurface(0,6,11,6)
        self.front2 = self.image2.subsurface(0,18,5,9)
        self.back2 = self.image2.subsurface(5,18,5,9)
        self.left2= self.image2.subsurface(0,0,11,9)
        self.right2 = self.image2.subsurface(0,9,11,9)
        self.image = self.left1
        self.rect = self.image.get_rect()
        self.health = 5
        self.speed = 1
        self.airborne = False
        self.atk = 5
        self.type = "Rabbit"
        self.dest = None

npc.active_npcs["Rabbit"] = Rabbit