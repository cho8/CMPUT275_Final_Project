import pygame,mapmatrix
from pygame import sprite
from player import Player


#images

PLAYERIMG = "images/Gus.png"
CABIN = "images/Cabin.png"
GAMEMAP = "images/gamemap.png"
TREE = "images/tree1.png"
LOG = "images/log.png"
MOUNTAIN = "images/mountain.png"
MOUNTAIN_END = "images/mountainend.png"
SNOWY_TREE = "images/tree2.png"

def load(image,x,y):
     object = sprite.Sprite()
     object.image = pygame.image.load(image).convert_alpha()
     object.rect = object.image.get_rect()
     object.rect.x = x*20
     object.rect.y = y*20
     buildings.add(object)

#Starting Positions/Sizes

SCREENSIZE = (600,400)
pstart_x = 200
pstart_y = 200
bgx = 0
bgy = 0
player_speed = 5
map_matrix = mapmatrix.map_matrix

#Custom Events
UPDATEHUNGER = 25
#pygame.event.Event(pygame.USEREVENT)

#Initializations

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Survive!")
background = pygame.image.load(GAMEMAP).convert()
buildings = sprite.OrderedUpdates()
offscr_buildings = sprite.OrderedUpdates()
for i in range(60):
    for j in range(60):
        if map_matrix[i][j] == 1:
            load(TREE,j,i)
        elif map_matrix[i][j] == 2:
            load(CABIN,j,i) 
        elif map_matrix[i][j] == 3:
            load(LOG,j,i) 
        elif map_matrix[i][j] == 4:
            load(MOUNTAIN,j,i)
        elif map_matrix[i][j] == 5:
            load(MOUNTAIN_END,j,i)
        elif map_matrix[i][j] == 6:
            load(SNOWY_TREE,j,i)          
         

player = Player(pstart_x,pstart_y,PLAYERIMG)
    
