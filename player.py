import pygame
from pygame.sprite import Group


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None, imagefile1=None, imagefile2=None, imagefile3 = None,imagefile4 = None,imagefile5 = None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        self.player.x_pos = x_pos
        self.player.y_pos = y_pos
        self.player.imagefile1 = imagefile1
        self.player.imagefile2 = imagefile2
        self.player.imagefile3 = imagefile3
        self.player.imagefile4 = imagefile4
        self.player.imagefile5 = imagefile5
     

        #Put initial attributes here




        #
        self.player.image1 = pygame.image.load(imagefile1).convert_alpha()
        self.player.image2 = pygame.image.load(imagefile2).convert_alpha()
        self.player.image3 = pygame.image.load(imagefile3).convert_alpha()
        self.player.image4 = pygame.image.load(imagefile4).convert_alpha()
        self.player.image5 = pygame.image.load(imagefile5).convert_alpha()
        self.player.image = self.player.image1
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)


