import pygame, setup
from pygame import sprite
import random

def turn(spr):
    spr.dir = abs(spr.dir + random.randrange(-1,1))
    if spr.dir > 3:
       spr.dir = 0
def turnAround(spr):
    if spr.dir == 0:
        spr.dir = 2
    if spr.dir == 1:
        spr.dir = 3
    if spr.dir == 2:
        spr.dir = 0
    if spr.dir == 3:
        spr.dir = 1

def move(spr):
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
    if pygame.sprite.spritecollideany(spr,setup.buildings) != None:
        turnAround(spr)
        move(spr)
        turn(spr)
        

def updateNPC(spritegroup):
    for spr in spritegroup:
        mv = random.randrange(0,15)
        if mv == 0:
            turn(spr)
        else:
            move(spr)

    spritegroup.draw(setup.screen)
    