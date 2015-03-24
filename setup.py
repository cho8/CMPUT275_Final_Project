import pygame,mapmatrix
from pygame import sprite
from player import Player


#images

PLAYERIMG = "images/Gus.png"
CABIN = "images/Cabin.png"
GAMEMAP = "images/gamemap.png"
TREE = "images/tree1.png"

def load(image,x,y):
     object = sprite.Sprite()
     object.image = pygame.image.load(image).convert_alpha()
     object.rect = object.image.get_rect()
     object.rect.x = x*20
     object.rect.y = y*20
     buildings.add(object)

#Starting Positions/Sizes

SCREENSIZE = (400,400)
pstart_x = 200
pstart_y = 200
bgx = 0
bgy = 0
player_speed = 5
map_matrix = mapmatrix.map_matrix

#Initializations
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Survive!")
background = pygame.image.load(GAMEMAP).convert()
buildings = sprite.Group()
for i in range(60):
    for j in range(60):
        if map_matrix[j][i] == 1:
            load(TREE,i,j)
        elif map_matrix[j][i] == 2:
            load(CABIN,i,j)           

player = Player(pstart_x,pstart_y,PLAYERIMG)
    
