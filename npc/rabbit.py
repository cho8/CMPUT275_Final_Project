import pygame, npc
from npc import BaseNPC
from tiles import Tile

class Rabbit(BaseNPC):
    """
    Prey NPC class.
    
    Modes Flight, Neutral
    """

    sprite = pygame.image.load("images/rabbit.png")

    def __init__(self, **keywords):
        self._base_image = Rabbit.sprite

        # Set base class
        super().__init__(**keywords)

        self.health = 10
        self.speed = 5
        self.atk = 5
        self.type = "Rabbit"

npc.active_npcs["Rabbit"] = Rabbit