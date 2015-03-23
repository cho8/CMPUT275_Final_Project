import pygame
from pygame import sprite
from player import Player
from background import Background

#images

PLAYERFRONT = "images/Gus_Front1.png"
PLAYERFRONT2 = "images/Gus_Front2.png"
PLAYERBACK = "images/Gus_Back1.png"
PLAYERLEFT = "images/Gus_Left.png"
PLAYERRIGHT = "images/Gus_Right.png"
CABIN = "images/Cabin.png"
GAMEMAP = "images/gamemap.png"
SCREENSIZE = (400,400)
pstart_x = 20
pstart_y = 20



screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Survive!")
background = pygame.image.load(GAMEMAP).convert()
bgx = 0
bgy = 0

cabin = sprite.Sprite()
cabin.image = pygame.image.load(CABIN).convert_alpha()
cabin.rect = cabin.image.get_rect()
cabin.rect.x = bgx + 50
cabin.rect.y = bgx + 50
buildings = sprite.Group()
buildings.add(cabin)
player = Player(pstart_x,pstart_y,PLAYERFRONT,PLAYERFRONT2,PLAYERBACK, PLAYERLEFT,PLAYERRIGHT)
