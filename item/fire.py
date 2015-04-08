import pygame, item
from item.base_item import BaseItem

class Fire(BaseItem):
    """
    Non-consumable. Hurts player if they stand too close to it.
    """

    def __init__(self):
        super().__init__()

        self.name = "Fire"
        self.type = "Tool"

        self.size = 20
        self.heal_value = -20
        self.timer = 0

        self._ground = True
        self.baseimage = pygame.image.load("images/item_fire.png").convert_alpha()
        self.front1 = self.baseimage.subsurface(0,0,20,20)
        self.front2 = self.baseimage.subsurface(20,0,20,20)
        self.image = self.front1    
        self.lastfront = self.front1

    def consume_item(self, player):
        """
        Consumes (uses) the item.
        Overrides base class definition of method.
        """
        # Overrides base class consumable
        # Cannot pick up from ground.
        if self.on_ground:
            return


