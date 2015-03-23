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
     

        #Put initial attributes here




        #
        self.player.image = self.player.front
        self.player.rect = self.player.front.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)


