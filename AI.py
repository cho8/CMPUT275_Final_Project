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

def move(spr):
    if spr.dir == 0:
        spr.image = spr.front
        spr.rect.y += spr.speed
    elif spr.dir == 1:
        spr.image = spr.left
        spr.rect.x -= spr.speed
    elif spr.dir == 2:
        spr.image = spr.back
        spr.rect.y -= spr.speed
    elif spr.dir == 3:
        spr.image = spr.right
        spr.rect.x += spr.speed
    checkCollisions(spr)
    print("x:{},y:{}".format(spr.rect.x,spr.rect.y))

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
    if spr.rect.x < 0:
        spr.rect.x = 0
        turnLeft(spr)
        turnLeft(spr)
    if spr.rect.x > setup.background.get_width():
        spr.rect.x = setup.background.get_width()
        turnLeft(spr)
        turnLeft(spr)
    if spr.rect.y < 0:
        spr.rect.y = 0
        turnLeft(spr)
        turnLeft(spr)
    if spr.rect.y > setup.background.get_height():
        spr.rect.x = setup.background.get_height()
        turnLeft(spr)
        turnLeft(spr)
        

def updateNPC(spritegroup):
    for spr in spritegroup:
        mv = random.randrange(0,200)
        if mv == 0:
            turnLeft(spr)
        elif mv == 1:
            turnRight(spr)
        elif mv == 2 or mv == 3 or mv == 4:
            pass # do nothing
        else:
            move(spr)
    