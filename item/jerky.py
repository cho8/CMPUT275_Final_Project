import pygame, item
from item.base_item import BaseItem
from pygame.sprite import Sprite
from random import randint

class Jerky(BaseItem):
    """
    Consumable item.
    Dry meat. It doesn't look sanitary.
    Restores hunger by a medium amount. Reduces health slightly.
    """
    def __init__(self):
        super().__init__()

        self.name = "Dry Jerky"
        self.type = "Consumable"
        self.description = item.descriptions[self.name]
        
        self.size = 5
        self.heal_value = randint(-10,10)
        self.stam_value = 10
        self.hung_value = -5

        self.image = pygame.image.load("images/item_jerky.png").convert_alpha()

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