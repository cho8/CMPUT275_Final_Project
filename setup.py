import pygame
from pygame import sprite

class Setup():

    PLAYERFRONT = "images/Gus_Front1.png"
    PLAYERFRONT2 = "images/Gus_Front2.png"
    PLAYERBACK = "images/Gus_Back1.png"
    PLAYERLEFT = "images/Gus_Left.png"
    PLAYERRIGHT = "images/Gus_Right.png"
    CABIN = "images/Cabin.png"
    pstart_x = 20
    pstart_y = 20



    screen = pygame.display.set_mode((400,400))
    pygame.init()
    back_x = 0
    back_y = 0
    background = pygame.image.load("images/gamemap.png").convert()
    cabin = sprite.Sprite()
    cabin.image = pygame.image.load(CABIN).convert_alpha()
    cabin.rect = cabin.image.get_rect()
    cabin.rect.x = back_x + 50
    cabin.rect.y = back_y + 50
    buildings = sprite.Group()
    buildings.add(cabin)
    buildings.draw(background)
    screen.blit(background, (back_x,back_y))
