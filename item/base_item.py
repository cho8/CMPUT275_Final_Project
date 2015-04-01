import pygame, item
from pygame.sprite import Sprite


SIZE = 20
L_WIDTH = 180
L_HEIGHT = 40

class BaseItem(Sprite):
    """
    Basic representation of items that can be found around the playable area.
    Includes sprites, stat changes and effects.
    """
    
    def __init__(self):
        
        Sprite.__init__(self)
        
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
        self.list_rect = pygame.Rect(0,0, L_WIDTH, L_HEIGHT)
        
        
    @property
    def on_ground(self):
        """
        Returns whether this item is on the ground.
        """
        return self._ground
    
    @property
    def in_inventory(self):
        return self._inventory
    
    def set_inventory(self):
        self._inventory = True
        self._ground = False
    
    def set_ground(self):
        self._inventory = False
        self._ground = True

    def consume_item(self):
        """
        Consumes the item and applies stat changes to the player character.
        Subclasses inherit this method and override it for specific stat changes.
        """
        if in_inventory(self):
            self._inventory = False

    def pick_up(self,inventory):
        """
        Changes item location from ground to inventory
        """
        if self.on_ground:
            self.set_inventory()
            # update inventory to have item
            inventory.append(self)

    def discard(self,inventory):
        if in_inventory(self):
            self._inventory = False
            inventory.pop(self)




