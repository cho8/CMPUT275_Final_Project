import pygame, item
from item.base_item import BaseItem
from pygame.sprite import Sprite

class Jerky(BaseItem):
    """
    Consumable item.
    Dry meat. It doesn't look sanitary.
    Restores hunger by a medium amount. Reduces health slightly.
    """
    sprite = pygame.image.load("images/item_oldwaterbottle.png")
    def __init__(self):
        super().__init__()

        self.name = "Dry Jerky"
        self.description = item.descriptions[self.name]
        
        self.heal_value = -10
        self.stam_value = 40
        self.image = pygame.image.load("images/item_oldwaterbottle.png").convert_alpha()

    def consume_item(self, player):
        """
        Consumes the item.
        Overrides base class definition of method.
        """
        super().consume_item(self)
        # add stats to player
        # player.stamina += self.heal_value
        # player.stamina += self.stam_value