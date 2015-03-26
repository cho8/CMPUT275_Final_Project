import pygame, item
from pygame.sprite import Sprite

class Berries(BaseItem):
    """
    Consumable item.
    Berries found in the wild are definitely safe to consume.
    Restores a bit of hunger and stamina.
    """
    def __init__(self):
        super().__init__(**keywords)

        self.name = "Berries"   

        self.eat_value = 10
        self.stam_value = 0
        self.image = pygame.image.load("images/item_berries.png").convert_alpha()

    def consume_item(self, player):
        """
        Consumes the item.
        Overrides base class definition of method.
        """
        super().consume_item(self):
        # add stats to player
        # player.hunger += self.eat_value
        # player.stamina += self.stam_value

