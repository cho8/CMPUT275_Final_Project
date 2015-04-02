import pygame,mapmatrix, npc, gui
from item.jerky import Jerky
from item.oldwaterbottle import OldWaterBottle
from pygame import sprite
from player import Player
from npc.wolf import Wolf
from npc.rabbit import Rabbit


#images

PLAYERIMG = "images/Gus.png"
PLAYERIMG2 = "images/Gus2.png"
CABIN = "images/Cabin.png"
GAMEMAP = "images/gamemap.png"
TREE = "images/tree1.png"
LOG = "images/log.png"
MOUNTAIN = "images/mountain.png"
MOUNTAIN_END = "images/mountainend.png"
SNOWY_TREE = "images/tree2.png"
WOLF = "images/wolf.png"
JERKY = "images/item_jerky.png"
GRASS = "images/grass.png"
RABBIT ="images/rabbit.png"
BOTTLE ="images/item_oldwaterbottle.png"

FRAMERATE = 8
frame = FRAMERATE

def load(image,x,y,group):
     if group == npcs:
         if image == WOLF:
             object = Wolf()
         elif image == RABBIT:
             object = Rabbit()
         object.rect.x = x*20
         object.rect.y = y*20
         group.add(object)
     elif group == items:
         if image == JERKY:
             object = Jerky()
             object.rect = object.image.get_rect()
             object.rect.x = x*20
             object.rect.y = y*20
             group.add(object)
             object.set_ground()
         if image == BOTTLE:
             object = OldWaterBottle()
             object.rect = object.image.get_rect()
             object.rect.x = x*20
             object.rect.y = y*20
             group.add(object)
             object.set_ground()
     else:
         object = sprite.Sprite()
         object.image = pygame.image.load(image).convert_alpha()
         object.rect = object.image.get_rect()
         object.rect.x = x*20
         object.rect.y = y*20
         group.add(object)

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
for i in range(60):
    for j in range(60):
        
        if map_matrix[i][j] == 'p':
            player = Player(j*20,i*20,PLAYERIMG,PLAYERIMG2)
        elif map_matrix[i][j] == 'w':
            load(WOLF,j,i,npcs)
        elif map_matrix[i][j] == 'r':
            load(RABBIT,j,i,npcs)
        elif map_matrix[i][j] == 1:
            load(TREE,j,i,trees)
        elif map_matrix[i][j] == 2:
            load(CABIN,j,i,buildings) 
        elif map_matrix[i][j] == 3:
            load(LOG,j,i,buildings) 
        elif map_matrix[i][j] == 4:
            load(MOUNTAIN,j,i,buildings)
        elif map_matrix[i][j] == 5:
            load(MOUNTAIN_END,j,i,buildings)
        elif map_matrix[i][j] == 6:
            load(SNOWY_TREE,j,i,buildings)
        elif map_matrix[i][j] == 9:
            load(JERKY,j,i,items)
        elif map_matrix[i][j] == 7:
            load(GRASS,j,i,longgrass)
        elif map_matrix[i][j] == 8:
            #boundary trees
            load(TREE,j,i,buildings)
        elif map_matrix[i][j] == 'b':
            load(BOTTLE,j,i,items)

                 
         
gui = gui.GUI()
    
