import pygame, item
from item.base_item import BaseItem

class Fire(BaseItem):
    """
    Non-consumable
    """

    def __init__(self):
        super().__init__()

        self.name = "Fire"
        self.type = "Tool"

        self.size = 20
        self.heal_value = -20

        self._ground = True
        self.image = pygame.image.load("images/item_fire.png").convert_alpha()
        self.subimage1 = self.image.subsurface(0,0,20,20)
        self.subimage2 = self.image.subsurface(20,0,20,20)
    
        self.lastimage = [self.subimage1, self.subimage2]
        self.image = self.subimage1

    def consume_item(self, player):
        """
        Consumes (uses) the item.
        Overrides base class definition of method.
        """
        # Overrides base class consumable
        # Cannot pick up from ground.
        if self.on_ground:
            return
