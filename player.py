import pygame
from pygame.sprite import Group


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None, imagemap=None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        self.player.x_pos = x_pos
        self.player.y_pos = y_pos
        imagemap = pygame.image.load(imagemap).convert_alpha()
        self.player.front = imagemap.subsurface(0,0,12,20)
        self.player.back = imagemap.subsurface(12,0,12,20)
        self.player.left= imagemap.subsurface(24,0,10,20)
        self.player.right = imagemap.subsurface(34,0,10,20)
     

        #Initial attributes
        self.health = 100 #percent
        self.hunger = 0
        self.alive = True
        self.starving = False
        self.encumbrance = 0
        self.stamina = 0
        self.exhausted = False

        self.player.image = self.player.front
        self.player.rect = self.player.front.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)

    def updateHunger(self):
        if self.hunger < 100:
            self.hunger += 1
        else:
            self.starving = True
            print("starving")
            print(self.health)
    def updateStamina(self):
        if self.stamina < 100:
            self.stamina -= 1+(self.encumbrance%25)
        else:
            self.exhausted = True

    def updatePlayer(self):
        #Takes roughly 4 min. from full health to death when starving.
        if self.starving:
            self.health -= .1
        if self.health <= 0:
            self.alive = False
            
