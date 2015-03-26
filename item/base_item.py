import pygame, item
from pygame.sprite import Sprite


SIZE = 20

class BaseItem(Sprite):
    """
    Basic representation of items that can be found around the playable area.
    Includes sprites, stat changes and effects.
    """
    
    def __init__(self):
        
        Sprite.__init__(self, items)
        
        self.name = "Base Item"
        self.description = self.description = item.descriptions[self.name]

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
        """
        Consumes the item and applies stat changes to the player character.
        Subclasses inherit this method and override it.
        """
        if in_inventory(self):
            self._inventory = False

    def pick_up(self):
        """
        Changes item location from ground to inventory
        """
        if on_ground(self):
            self._ground = False
            self._inventory = True
            # update inventory to have item
            item.active_inventory[self.name] = self

    def discard(self):
        if in_inventory(self) and self.name in item.active_inventory:
            self._inventory = False
            item.active_inventory.pop(self.name)




