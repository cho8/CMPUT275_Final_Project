import pygame, setup, animation
from pygame import sprite
from item import *
import random

def turnLeft(spr):
    spr.dir += 1
    if spr.dir > 3:
       spr.dir = 0
def turnRight(spr):
    spr.dir -= 1
    if spr.dir < 0:
       spr.dir = 3
def flee(spr):

    if nearPlayer(spr,120):
        if setup.player.player.rect.x <= spr.rect.x and setup.player.dir == 3:
            spr.dir = 3
        elif setup.player.player.rect.x > spr.rect.x and setup.player.dir == 1:
            spr.dir = 1
        elif setup.player.player.rect.y <= spr.rect.y and setup.player.dir == 0:
            spr.dir = 0
        elif setup.player.player.rect.y > spr.rect.y and setup.player.dir == 2:
            spr.dir = 2
        move(spr)
    elif pygame.sprite.spritecollideany(spr,setup.trees) != None:
        move(spr)
    else:
        spr.mode = "Neutral"
        spr.speed /= 5
        
def manDist(spr1,spr2):
    x = abs(spr1.rect.x - spr2.rect.x)
    y = abs(spr1.rect.y - spr2.rect.y)
    return x+y

def nearPlayer(spr, minDist = 30):
    
    if manDist(spr,setup.player.player) < minDist:
        return True
    else:
        return False

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
    animation.handleAnimation(spr,spr.dir)

def checkCollisions(spr):
    if spr.mode == "Flight":
        if pygame.sprite.spritecollideany(spr,setup.trees) != None\
        and pygame.sprite.spritecollideany(spr,setup.buildings) == None:
            return
    if pygame.sprite.spritecollideany(spr,setup.buildings) != None\
    or pygame.sprite.spritecollideany(spr,setup.player) != None\
    or pygame.sprite.spritecollideany(spr,setup.trees) != None\
    or pygame.sprite.spritecollideany(spr,setup.items) ==  fire.Fire()\
    and spr.mode != "Flight":
        if spr.dir == 0:
            spr.rect.y -= spr.speed
        elif spr.dir == 1:
            spr.rect.x += spr.speed
        elif spr.dir == 2:
            spr.rect.y += spr.speed
        elif spr.dir == 3:
            spr.rect.x -= spr.speed
        turn = random.randint(0,1)
        if turn == 0: 
            turnLeft(spr)
        else:
            turnRight(spr)
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

        if spr.type == "Rabbit" and nearPlayer(spr) and spr.mode is not "Flight":
            spr.mode = "Flight"
            spr.speed *= 5
        if spr.mode == "Neutral":
            move(spr)
        elif spr.mode == "Flight":
            flee(spr)
         
    