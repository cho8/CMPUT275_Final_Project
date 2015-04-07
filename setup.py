import pygame,mapmatrix, npc, gui
from item import *
from pygame import sprite
from player import Player
from npc import *


#images

CABIN = "images/Cabin.png"
GAMEMAP = "images/gamemap.png"
TREE = "images/tree1.png"
LOG = "images/log.png"
MOUNTAIN = "images/mountain.png"
MOUNTAIN_END = "images/mountainend.png"
SNOWY_TREE = "images/tree2.png"
GRASS = "images/grass.png"

FRAMERATE = 6
frame = FRAMERATE

#Object loading functions

def loadSprite(image,x,y,group):
     object = sprite.Sprite()
     object.image = pygame.image.load(image).convert_alpha()
     object.rect = object.image.get_rect()
     object.rect.x = x*20
     object.rect.y = y*20
     group.add(object)

def loadNPC(npc,x,y):
    if npc == "wolf":
        object = wolf.Wolf()
    elif npc == "rabbit":
        object = rabbit.Rabbit()
    object.rect.x = x*20
    object.rect.y = y*20
    npcs.add(object)

def loadItem(object,x,y):

    object.rect = object.image.get_rect()
    object.rect.x = x*20
    object.rect.y = y*20
    object.set_ground()
    items.add(object)

#Starting Positions/Sizes

SCREENSIZE = (600,400)
pstart_x = 200
pstart_y = 200
bgx = 0
bgy = 0
map_matrix = mapmatrix.map_matrix

#Custom Events
UPDATESTATUS = 25
MOVE_NPCS = 26
#pygame.event.Event(pygame.USEREVENT)

#Initializations

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Survive!")
background = pygame.image.load(GAMEMAP).convert()
buildings = sprite.OrderedUpdates()
trees = sprite.OrderedUpdates()
npcs = sprite.Group()
items = sprite.Group()
longgrass = sprite.Group()

# loading map

for i in range(60):
    for j in range(60):
        
        if map_matrix[i][j] == 'p':
            player = Player(j*20,i*20)
        elif map_matrix[i][j] == 'w':
            loadNPC("wolf",j,i)
        elif map_matrix[i][j] == 'r':
            loadNPC("rabbit",j,i)

        elif map_matrix[i][j] == 1:
            loadSprite(TREE,j,i,trees)
        elif map_matrix[i][j] == 2:
            loadSprite(CABIN,j,i,buildings) 
        elif map_matrix[i][j] == 3:
            loadSprite(LOG,j,i,buildings) 
        elif map_matrix[i][j] == 4:
            loadSprite(MOUNTAIN,j,i,buildings)
        elif map_matrix[i][j] == 5:
            loadSprite(MOUNTAIN_END,j,i,buildings)
        elif map_matrix[i][j] == 6:
            loadSprite(SNOWY_TREE,j,i,trees)
        elif map_matrix[i][j] == 7:
            loadSprite(GRASS,j,i,longgrass)

        #boundary trees
        elif map_matrix[i][j] == 8:
            loadSprite(TREE,j,i,buildings)
        elif map_matrix [i][j] == 9:
            loadSprite(SNOWY_TREE,j,i,buildings)

        #items
        elif map_matrix[i][j] == 'j':
            loadItem(jerky.Jerky(),j,i)
        elif map_matrix[i][j] == 'wb':
            loadItem(oldwaterbottle.OldWaterBottle(),j,i)
        elif map_matrix[i][j] == 'b':
            loadItem(berries.Berries(),j,i)
        elif map_matrix[i][j] == 'f':
            loadItem(fire.Fire(),j,i)
        elif map_matrix[i][j] == 'fw':
            loadItem(firewood.Firewood(),j,i)

                 
gui = gui.GUI()

    
