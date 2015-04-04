import pygame, item
from item.base_item import BaseItem
from pygame.sprite import Sprite
import setup, gui

class Firewood(BaseItem):
    """
    Fuel for a fire.
    When used it drops on the ground at the player's location
    """

    def __init__(self):
        super().__init__()

        self.name = "Dry Jerky"
        self.type = "Tool"
        self.description = item.descriptions[self.name]

        self.size = 20

        self.image = pygame.image.load("image/item_firewood.png").convert_alpha()

    def consume_item(self, player):
        """
        Consumes (uses) the item.
        Overrides base class definition of method.
        """
        # if the player is standing on something, do nothing
        if pygame.sprite.sprigecollideany(player, setup.items):
            return
        
        super().consume_item(player)
        #place item on floor
        setup.loadItem(self,player.x_pos, player.y_pos)
        self._ground = True
        self._inventory = False
