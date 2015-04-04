import pygame, item
from item.base_item import BaseItem
from pygame.sprite import Sprite
import gui

class Flint(BaseItem):
    """
    Consumable Item.
    Fuel for a fire.
    When used it drops on the ground at the player's location
    """

    def __init__(self):
        super().__init__()

        self.name = "Flint"
        self.type = "Tool"
        self.description = item.descriptions[self.name]

        self.size = 10

        self.image = pygame.image.load("image/item_flint.png").convert_alpha()

    def consume_item(self, player):
        """
        Consumes (uses) the item.
        Overrides base class definition of method.
        """
        # Check if the item on the ground is firewood. If it is, remove both items
        # and load 'campfire'
        item_at_pos = pygame.sprite.sprigecollideany(player, setup.items)
        if item_at_pos.name == "Firewood":
            super().consume_item(player)
            gui.remove(item_at_pos)
            new_fire = item.campfire.Campfire()
            new_fire.rect = new_fire.image.get_rect()
            new_fire.rect.x, new_fire.rect.y = player.x_pos+20, player.y_pos
            new_fire.set_ground()
            gui.buildings.add(new_fire)
