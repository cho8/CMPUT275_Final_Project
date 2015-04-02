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
def findRefuge(spr):
    """
    if spr.dest is not None:
        closest = None
        cdist = setup.screen.get_width()
        for grass in setup.longgrass:
            dist = manDist(spr,grass) 
            if dist < cdist:
                cdist = dist
                closest = grass
        spr.dest = closest
    moveDest(spr)
    """
    if manDist(spr,setup.player.player)<120:
        spr.dir = setup.player.dir
        if spr.dir > 3:
            spr.dir = 0
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

def nearPlayer(spr):
    
    if manDist(spr,setup.player.player) < 30:
        return True
    else:
        return False

def moveDest(spr):
        if spr.rect.x < spr.dest.rect.x:
            spr.dir = 3
        elif spr.rect.x > spr.dest.rect.x: 
            spr.dir = 1
        if spr.rect.y > spr.dest.rect.y:
            spr.dir = 2
        elif spr.rect.y < spr.dest.rect.y:
            spr.dir = 0
        if manDist(spr,spr.dest)<5:
            spr.dest = None
            spr.mode = "Neutral"
            return
        move(spr)

def getImage(spr):
    if spr.dir == 0:
        spr.image = spr.front
        spr.rect.size = spr.image.get_size()
        if spr.type == "Rabbit":
            if setup.frame % setup.FRAMERATE == 0:
                   if not spr.airborne:
                       spr.rect.y -= 3
                       spr.airborne = True
                   else:
                       spr.rect.y += 3
                       spr.airborne = False

    elif spr.dir == 2:
        spr.image = spr.back
        spr.rect.size = spr.image.get_size()
        if spr.type == "Rabbit":
            if setup.frame % setup.FRAMERATE == 0:
                   if not spr.airborne:
                       spr.rect.y -= 3
                       spr.airborne = True
                   else:
                       spr.rect.y += 3
                       spr.airborne = False

    elif spr.dir == 1:
        if spr.type == "Rabbit":
 
            spr.image = spr.left
            spr.rect.size = spr.image.get_size()

            if setup.frame % setup.FRAMERATE == 0:
                if not spr.airborne:
                    spr.rect.y -= 3
                    spr.airborne = True
                else:
                    spr.rect.y += 3
                    spr.airborne = False
        else:
            if setup.frame % setup.FRAMERATE == 0:
                if spr.image == spr.left1:
                    spr.image = spr.left2
                else:
                    spr.image = spr.left1
            spr.rect.size = spr.image.get_size()

    elif spr.dir == 3:
        if spr.type == "Rabbit":
 
            spr.image = spr.right
            spr.rect.size = spr.image.get_size()

            if setup.frame % setup.FRAMERATE == 0:
                if not spr.airborne:
                    spr.rect.y -= 3
                    spr.airborne = True
                else:
                    spr.rect.y += 3
                    spr.airborne = False
        else:
            if setup.frame % setup.FRAMERATE == 0:
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
    if spr.mode == "Flight":
        if pygame.sprite.spritecollideany(spr,setup.trees) != None:
            return
    if pygame.sprite.spritecollideany(spr,setup.buildings) != None\
    or pygame.sprite.spritecollideany(spr,setup.player) != None\
    or pygame.sprite.spritecollideany(spr,setup.trees) != None:
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

        if spr.type == "Rabbit" and nearPlayer(spr) and spr.mode is not "Flight" :
            spr.mode = "Flight"
            spr.speed *= 5
            print("Flight")
        if spr.mode == "Neutral":
            mv = random.randrange(0,100)
            if mv == 0 or mv == 1 or mv == 2:
                turnLeft(spr)
            elif mv == 2 or mv == 3 or mv == 4:
                turnRight(spr)
            else:
                move(spr)
        elif spr.mode == "Flight":
            spr.dest = findRefuge(spr)
         
    