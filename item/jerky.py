import pygame, item
from pygame.sprite import Sprite

class Jerky(BaseItem):
    """
    Consumable item.
    Dry meat. It doesn't look sanitary.
    Restores hunger by a medium amount. Reduces health slightly.
    """
    sprite = pygame.image.load("images/item_oldwaterbottle.png")
    def __init__(self):
        super().__init__(**keywords)

        self.name = "Dry Jerky"
        self.description = ""
        
        self.heal_value = -10
        self.stam_value = 40

    def consume_item(self, player):
        """
        Consumes the item.
        Overrides base class definition of method.
        """
        super().consume_item(self):
        # add stats to player
        # player.stamina += self.heal_value
        # player.stamina += self.stam_value