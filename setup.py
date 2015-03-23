import pygame
from pygame import sprite
from player import Player

#images

PLAYERIMG = "images/Gus.png"
CABIN = "images/Cabin.png"
GAMEMAP = "images/gamemap.png"

#Starting Positions/Sizes

SCREENSIZE = (400,400)
pstart_x = 200
pstart_y = 200
bgx = 0
bgy = 0
player_speed = 5

#Initializations
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Survive!")
background = pygame.image.load(GAMEMAP).convert()
cabin = sprite.Sprite()
cabin.image = pygame.image.load(CABIN).convert_alpha()
cabin.rect = cabin.image.get_rect()
cabin.rect.x = 50
cabin.rect.y = 50
buildings = sprite.Group()
buildings.add(cabin)
player = Player(pstart_x,pstart_y,PLAYERIMG)
