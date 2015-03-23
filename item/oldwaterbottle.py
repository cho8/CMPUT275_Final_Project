import pygame, item
from pygame.sprite import Sprite

class OldWaterBottle(BaseItem):
    """
    Consumable item.
    A bottle of water.
    Restores stamina by a medium amount.
    """
    sprite = pygame.image.load("images/item_oldwaterbottle.png")
    def __init__(self):
        super().__init__(**keywords)

        self.name = "Old Water Bottle"
        self.description = ""
    
        self.stam_value = 40

    def consume_item(self, player):
        """
        Consumes the item.
        Overrides base class definition of method.
        """
        super().consume_item(self):
        # add stats to player
        # player.stamina += self.stam_value