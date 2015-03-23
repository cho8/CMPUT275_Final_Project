import pygame
from pygame import Surface

class Background(Surface):

    def __init__(self,image,x= 0 ,y= 0):
        self.image = pygame.image.load(image).convert()
        size = (self.image.get_width(),self.image.get_height())
        Surface.__init__(self,size)
        self = self.image
        self.x = x
        self.y = y