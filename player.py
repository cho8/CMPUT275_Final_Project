import pygame,setup,animation
from pygame.sprite import Group
from item import *


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        gus1 = pygame.image.load("images/gus1.png").convert_alpha()
        gus2 = pygame.image.load("images/gus2.png").convert_alpha()
        self.player.front1 = gus1.subsurface(0,0,12,20)
        self.player.back1 = gus1.subsurface(12,0,12,20)
        self.player.left1= gus1.subsurface(24,0,10,20)
        self.player.right1 = gus1.subsurface(34,0,10,20)
        self.player.front2 = gus2.subsurface(0,0,12,20)
        self.player.back2 = gus2.subsurface(12,0,12,20)
        self.player.left2= gus2.subsurface(24,0,10,20)
        self.player.right2 = gus2.subsurface(34,0,10,20)
        self.player.type = "Player"  

        #Initial attributes
        self.health = 100 #percent
        self.hunger = 0
        self.alive = True
        self.starving = False
        self.encumbrance = 0
        self.stamina = 100
        self.encumbered = False
        self.exhausted = False
        self.basespeed = 2
        self.player.dir = 0
        self.inventory = []
        self.moving = False
        self.player.image = self.player.front1
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)
        self.player.running = False
        self.adjustx = 1
        self.adjusty = 1
        self.player.lastleft = self.player.left1
        self.player.lastright = self.player.right1
        self.player.lastback = self.player.back1
        self.player.lastfront = self.player.front1
        

    def updateHunger(self):
        if self.hunger < 100:
            self.hunger += 1 + (int((100 - self.stamina)/20))
        else:
            self.starving = True
            print("starving")
            print(self.health)

    def nearFire(self):
        for item in setup.items:
            if item.name == "Fire":
                if abs(item.rect.x-self.player.rect.x) < 30\
                or abs(item.rect.x-self.player.rect.x) < 30:
                    return True
        return False 

    def updateStamina(self):
        if self.moving == True:
            self.staminaloss = .01 + (self.encumbrance/25)*.01
            if self.player.running:
                self.staminaloss *= 2
                self.player.running = False
            if self.stamina > -5:
                self.stamina -= self.staminaloss
            if self.stamina < 0:
                self.exhausted = True
            self.moving = False
        else:
            if self.stamina < 100:
                if self.nearFire():
                    self.stamina += .02
                else:
                    self.stamina += .01
            if self.stamina > 0:
                self.exhausted = False

    def movePlayer(self,direction):
        SPEED = self.basespeed
        VIEWDISTANCE = 150
        GUIWIDTH = 200
        self.moving = True
        if self.encumbrance > 75:
            self.encumbered = True
            SPEED/=2
        else:
            self.encumbered = False
        if self.player.running:
            SPEED *= 2
        if pygame.sprite.spritecollideany(self.player,setup.longgrass) != None\
        or self.encumbered or self.exhausted: 
            self.player.running = False
            SPEED = 1
        else:

            if self.player.rect.x % 2 != 0:
                print("adjusting x")
                if self.adjustx == 1:
                    self.adjustx = -1
                else:
                    self.adjusty = 1
                self.player.rect.x += self.adjustx
            if self.player.rect.y % 2 != 0:
                print("adjusting y")
                if self.adjusty == 1:
                    self.adjusty = -1
                else:
                    self.adjusty = 1
                self.player.rect.y += self.adjusty

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                self.dir = 1
                SPEED *= -1                

            else:
                self.dir = 3
 
            if self.player.rect.x < VIEWDISTANCE:               
                if setup.gui.bgx < 0:
                    self.player.rect.x = VIEWDISTANCE
                    setup.gui.bgx -= SPEED
                    
                    for rect in setup.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED
                    for item in setup.items:
                        item.rect.x -= SPEED
                    for object in setup.longgrass:
                        object.rect.x -= SPEED
                    for object in setup.trees:
                        object.rect.x -= SPEED

            elif self.player.rect.x > setup.screen.get_width()-VIEWDISTANCE-GUIWIDTH:
                if setup.gui.bgx >(0-setup.background.get_width()\
                +setup.screen.get_width()-GUIWIDTH):
                    self.player.rect.x = setup.screen.get_width()-VIEWDISTANCE-GUIWIDTH
                    setup.gui.bgx -= SPEED
                
                    for rect in setup.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED
                    for item in setup.items:
                        item.rect.x -= SPEED
                    for object in setup.longgrass:
                        object.rect.x -= SPEED
                    for object in setup.trees:
                        object.rect.x -= SPEED

            self.player.rect.x += SPEED

            if pygame.sprite.spritecollideany(self.player,setup.buildings) != None\
            or pygame.sprite.spritecollideany(self.player,setup.npcs) != None\
            or pygame.sprite.spritecollideany(self.player,setup.trees) != None:

                self.player.rect.x -= SPEED

            if type(pygame.sprite.spritecollideany(self.player,setup.items)) == fire.Fire:
                self.player.rect.x -= SPEED*4
                self.health -= 2

        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                self.dir = 2
                SPEED *= -1

            else:
                self.dir = 0

            if self.player.rect.y > setup.screen.get_height() - VIEWDISTANCE: 
                if setup.gui.bgy >(0-setup.background.get_height()\
                +setup.screen.get_height()):
                    self.player.rect.y = setup.screen.get_height()-VIEWDISTANCE         
                    setup.gui.bgy -= SPEED
                    
                    for rect in setup.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED
                    for item in setup.items:
                        item.rect.y -= SPEED
                    for object in setup.longgrass:
                        object.rect.y -= SPEED
                    for object in setup.trees:
                        object.rect.y -= SPEED
            
            elif self.player.rect.y < VIEWDISTANCE:
                if setup.gui.bgy < 0:
                    self.player.rect.y = VIEWDISTANCE
                    setup.gui.bgy -= SPEED
                
                    for rect in setup.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED
                    for item in setup.items:
                        item.rect.y -= SPEED
                    for object in setup.longgrass:
                        object.rect.y -= SPEED
                    for object in setup.trees:
                        object.rect.y -= SPEED

            self.player.rect.y += SPEED
            if pygame.sprite.spritecollideany(self.player,setup.buildings) != None\
            or pygame.sprite.spritecollideany(self.player,setup.npcs) != None\
            or pygame.sprite.spritecollideany(self.player,setup.trees) != None:

                self.player.rect.y -= SPEED

            if type(pygame.sprite.spritecollideany(self.player,setup.items)) == fire.Fire:
                self.player.rect.y -= SPEED*4
                self.health -= 2

        animation.handleAnimation(self.player,self.dir)

    def updatePlayer(self):

        #Takes roughly 4 min. from full health to death when starving.
        self.updateStamina()
            
        if self.starving:
            self.health -= .1
        if self.nearFire():
            if self.health < 100:
                self.health += .01
        if self.health <= 0:
            self.alive = False
            
