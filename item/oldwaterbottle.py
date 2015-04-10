import pygame, item
from item.base_item import BaseItem

class OldWaterBottle(BaseItem):
    """
    Consumable item.
    A bottle of water.
    Restores stamina by a medium amount.
    """
    
    def __init__(self):
        super().__init__()

        self.name = "Old Water Bottle"
        self.type = "Consumable"
        self.description = item.descriptions[self.name]
    
        self.stam_value = 20
        self.size = 10
        
        self.image = pygame.image.load("images/item_oldwaterbottle.png").convert_alpha()

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