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
        self.front = self.image.subsurface(0,12,5,6)
        self.back = self.image.subsurface(5,12,5,6)
        self.left= self.image.subsurface(0,0,11,6)
        self.right = self.image.subsurface(0,6,11,6)
        self.image = self.left
        self.rect = self.image.get_rect()
        self.health = 5
        self.speed = 6
        self.airborne = False
        self.atk = 5
        self.type = "Rabbit"

npc.active_npcs["Rabbit"] = Rabbit