import pygame, npc
from npc.base_npc import BaseNPC


class Rabbit(BaseNPC):
    """
    Prey NPC class.
    
    Modes Flight, Neutral
    """


    def __init__(self, **keywords):
        super().__init__(**keywords)
        self.image = pygame.image.load("images/rabbit2.png").convert_alpha()
        self.front = self.image.subsurface(0,21,9,11)
        self.back = self.image.subsurface(9,21,9,11)
        self.left= self.image.subsurface(0,0,16,10)
        self.right = self.image.subsurface(0,12,16,10)
        self.image = self.left
        self.rect = self.image.get_rect()
        self.health = 5
        self.speed = 1
        self.airborne = False
        self.atk = 5
        self.type = "Rabbit"
        self.dest = None

npc.active_npcs["Rabbit"] = Rabbit