import pygame, item
from item.base_item import BaseItem
from pygame.sprite import Sprite

class Berries(BaseItem):
    """
    Consumable item.
    Berries found in the wild are definitely safe to consume.
    Restores a bit of hunger and stamina.
    """
    def __init__(self):
        super().__init__()

        self.name = "Berries"
        self.type = "Consumable"
        self.description = item.descriptions[self.name]
        self.hung_value = -5
        self.stam_value = 0
        
        self.image = pygame.image.load("images/item_berries.png").convert_alpha()

    def consume_item(self, player):
        """
        Consumes the item.
        Overrides base class definition of method.
        """
        super().consume_item(player)
        # add stats to player
        player.health += self.heal_value
        if player.health > 100:
            player.health = 100
        
        player.stamina += self.stam_value
        if player.stamina > 100:
            player.stamina = 100
        
        player.hunger += self.hung_value
        if player.hunger < 0:
            player.hunger = 0

