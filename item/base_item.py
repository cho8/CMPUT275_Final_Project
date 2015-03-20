import pygame, item
from pygame.sprite import Sprite


SIZE = 20

class BaseItem(Sprite):
    """
    Basic representation of items that can be found around the playable area.
    Includes sprites, stat changes and effects.
    """
    #active_units = pygame.sprite.LayeredUpdates()
    
    def __init__(self):
        self.name = "Base Item"
        self.description = "Base Description"

        self.size = 10
        self.heal_value = 0
        self.eat_value = 0
        self.stam_value = 0
        
        self._inventory = False
        self._ground = False
        
        
    @property
    def on_ground(self):
        """
        Returns whether this item is on the ground.
        """
        return self._inventory

    def in_inventory(self):
        pass


