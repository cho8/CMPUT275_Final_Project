import pygame, item, gui
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
        self.type = "Base"
        self.description = self.description = item.descriptions[self.name]

        self.size = 10
        self.heal_value = 0
        self.hung_value = 0
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
        """
        Returns whether this item is in inventory.
        """
        return self._inventory
    
    def set_inventory(self):
        self._inventory = True
        self._ground = False
    
    def set_ground(self):
        self._inventory = False
        self._ground = True

    def consume_item(self, player):
        """
        Consumes the item and applies stat changes to the player character.
        Subclasses inherit this method and override it for specific stat changes.
        """
        if self.in_inventory:
            self.discard(player)
            self._inventory = False
            

    def pick_up(self,player):
        """
        Changes item location from ground to inventory
        """
        self.set_inventory()
        # update inventory to have item
        player.inventory.append(self)
        player.encumbrance += self.size

    def put_down(self, player):
        if self.in_inventory:
            self.set_ground()
            player.inventory.remove(self)
            player.encumbrance -= self.size
            self.rect.x, self.rect.y = player.x_pos, player.y_pos
            gui.items.add(self)

    def discard(self,player):
        if self.in_inventory:
            self._inventory = False
            self._ground = False
            player.inventory.remove(self)
            player.encumbrance -= self.size




