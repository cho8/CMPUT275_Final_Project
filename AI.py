import pygame, setup
from pygame import sprite
import random

def turnLeft(spr):
    spr.dir += 1
    if spr.dir > 3:
       spr.dir = 0
def turnRight(spr):
    spr.dir -= 1
    if spr.dir < 0:
       spr.dir = 3

def getImage(spr):
    if spr.dir == 0:
        spr.image = spr.front
        spr.rect.size = spr.image.get_size()

    elif spr.dir == 2:
        spr.image = spr.back
        spr.rect.size = spr.image.get_size()

    elif spr.dir == 1:
        if spr.type == "Rabbit":
 
            spr.image = spr.left
            spr.rect.size = spr.image.get_size()

            if not spr.airborne:
                spr.rect.y -= 3
                spr.airborne = True
            else:
                spr.rect.y += 3
                spr.airborne = False
        else:
            if spr.image == spr.left1:
                spr.image = spr.left2
            else:
                spr.image = spr.left1
            spr.rect.size = spr.image.get_size()

    elif spr.dir == 3:
        if spr.type == "Rabbit":
 
            spr.image = spr.right
            spr.rect.size = spr.image.get_size()

            if not spr.airborne:
                spr.rect.y -= 3
                spr.airborne = True
            else:
                spr.rect.y += 3
                spr.airborne = False
        else:
            if spr.image == spr.right1:
                spr.image = spr.right2
            else:
                spr.image = spr.right1
            spr.rect.size = spr.image.get_size()
    

def move(spr):
    getImage(spr)
    if spr.dir == 0:
        spr.rect.y += spr.speed
    elif spr.dir == 1:
        spr.rect.x -= spr.speed
    elif spr.dir == 2:
        spr.rect.y -= spr.speed
    elif spr.dir == 3:
        spr.rect.x += spr.speed
    checkCollisions(spr)

def checkCollisions(spr):
    if pygame.sprite.spritecollideany(spr,setup.buildings) != None or pygame.sprite.spritecollideany(spr,setup.player) != None:
        if spr.dir == 0:
            spr.rect.y -= spr.speed
        elif spr.dir == 1:
            spr.rect.x += spr.speed
        elif spr.dir == 2:
            spr.rect.y += spr.speed
        elif spr.dir == 3:
            spr.rect.x -= spr.speed 
        turnLeft(spr)
    if spr.rect.x < setup.gui.bgx:
        spr.rect.x = setup.gui.bgx
        turnLeft(spr)
        turnLeft(spr)
    if spr.rect.x > setup.background.get_width():
        spr.rect.x = setup.background.get_width()
        turnLeft(spr)
        turnLeft(spr)
    if spr.rect.y < setup.gui.bgy:
        spr.rect.y = setup.gui.bgy
        turnLeft(spr)
        turnLeft(spr)
    if spr.rect.y > setup.background.get_height():
        spr.rect.x = setup.background.get_height()
        turnLeft(spr)
        turnLeft(spr)
        

def updateNPC(spritegroup):
    for spr in spritegroup:
        mv = random.randrange(0,100)
        if mv == 0 or mv == 1 or mv == 2:
            turnLeft(spr)
        elif mv == 2 or mv == 3 or mv == 4:
            turnRight(spr)
        else:
            move(spr)
    