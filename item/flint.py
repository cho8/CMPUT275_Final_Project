import pygame, item
from item.base_item import BaseItem
import setup, gui

class Flint(BaseItem):
    """
    Consumable Item.
    When used on a tile with firewood it can create a fire.
    """

    def __init__(self):
        super().__init__()

        self.name = "Flint"
        self.type = "Tool"
        self.description = item.descriptions[self.name]

        self.size = 10

    def consume_item(self, player):
        """
        Consumes (uses) the item.
        Overrides base class definition of method.
        """
        # Check if the item on the ground is firewood. If it is, remove both items
        # and load 'campfire'
        item_at_pos = pygame.sprite.spritecollideany(player.player, setup.items)
        if item_at_pos and item_at_pos.name == "Firewood":
            super().consume_item(player)
            setup.items.remove(item_at_pos)
            new_fire = item.fire.Fire()
            new_fire.rect = new_fire.image.get_rect()
            new_fire.rect.y = player.player.rect.y
            new_fire.rect.x = player.player.rect.x

            if player.get_dir() == "DOWN":
                new_fire.rect.y = player.player.rect.y + 20
            elif player.get_dir() == "LEFT":
                new_fire.rect.x = player.player.rect.x - 30
            elif player.get_dir() == "UP":
                new_fire.rect.y = player.player.rect.y - 20
            elif player.get_dir() == "RIGHT":
                new_fire.rect.y = player.player.rect.x + 30
                
            setup.items.add(new_fire)





