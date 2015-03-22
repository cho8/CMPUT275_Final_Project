import pygame, item
from pygame.sprite import Sprite


SIZE = 20

class BaseItem(Sprite):
    """
    Basic representation of items that can be found around the playable area.
    Includes sprites, stat changes and effects.
    """
    
    def __init__(self,
                 x_pos = None,
                 y_pos = None,
                 **keywords):
        
        # There should be a group called "items" somewhere
        Sprite.__init__(self, items)
        
        self.name = "Base Item"
        self.description = "Base Description"
        
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.size = 10
        self.heal_value = 0
        self.eat_value = 0
        self.stam_value = 0
        
        self._inventory = False
        self._ground = False
    
    # pygame things
        self.image = None
        self.rect = pygame.Rect(0,0,SIZE, SIZE)
        
        
    @property
    def on_ground(self):
        """
        Returns whether this item is on the ground.
        """
        return self._inventory
    
    @property
    def in_inventory(self):
        return self._ground


    def consume_item(self):
        if in_inventory(self):
            self._inventory = False
            # subclasses inherit this method

    def pick_up(self):
        """
        Changes item location from ground to inventory
        """
        if on_ground(self):
            self._ground = False
            self._inventory = True
            # update inventory to have item
            item.active_inventory[self.name] = self




