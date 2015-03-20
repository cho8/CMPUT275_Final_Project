import pygame, item
from pygame.sprite import Sprite

size = 20

class BaseItem(Sprite):
    """
    Basic representation of items that can be found around the playable area.
    Includes sprites, stat changes and effects.
    """

    def __init__(self):
        self.name = "Base Item"
        self.description = "Base Description"

        self.