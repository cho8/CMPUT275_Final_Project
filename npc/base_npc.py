import pygame, npc
from pygame.sprite import Sprite

SIZE = 20

class BaseNPC(Sprite):
    """
    Base NPC respresentation for which predators and prey extend from.
    """

    #active_NPCs =  pygame.sprite.LayeredUpdates()

    def __init__(self,
                 x_pos = None,
                 y_pos = None):

        Sprite.__init(self)

        self.x_pos = x_pos
        self.y_pos = y_pos

        # Default Initialized values
        self.mode = "Neutral"
        self.health = 10
        self.speed = 10
        self.atk = 1
        self.type = "Base NPC"
        
        
        # Required pygame parameters
        self.image = none
        self.rect = pygame.Rect(0,0, SIZE, SIZE)
        
        if activate:
            self.activate()

    def set_npc_mode(self, mode):
        if mode == "Neutral"
            self.mode = "Neutral"
        if mode == "Fight"
            self.mode = "Fight"
        if mode == "Escape"
            self.mode = "Escape"



