import pygame, item
from item.base_item import BaseItem
import setup

class Firewood(BaseItem):
    """
    Fuel for a fire.
    When used it drops on the ground at the player's location.
    Flint can be used when standing by some firewood to create a fire.
    """

    def __init__(self):
        super().__init__()

        self.name = "Firewood"
        self.type = "Tool"
        self.description = item.descriptions[self.name]

        self.size = 20

        self.image = pygame.image.load("images/item_firewood.png").convert_alpha()

    def consume_item(self, player):
        """
        Consumes (uses) the item.
        Overrides base class definition of method.
        """
        # if the player is standing on something, do nothing
        if pygame.sprite.spritecollideany(player.player, setup.items):
            return
        
        super().consume_item(player)
        #place item on floor
        self.rect.x, self.rect.y = player.player.rect.x, player.player.rect.y
        setup.items.add(self)
        self._ground = True
        self._inventory = False
