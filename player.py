import pygame,setup
from pygame.sprite import Group


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        self.player.x_pos = x_pos
        self.player.y_pos = y_pos
        gus = pygame.image.load("images/gus.png").convert_alpha()
        gus1 = pygame.image.load("images/gus1.png").convert_alpha()
        gus2 = pygame.image.load("images/gus2.png").convert_alpha()
        self.player.front = gus.subsurface(0,0,12,20)
        self.player.back = gus.subsurface(12,0,12,20)
        self.player.left= gus.subsurface(24,0,10,20)
        self.player.right = gus.subsurface(34,0,10,20)
        self.player.front1 = gus1.subsurface(0,0,12,20)
        self.player.back1 = gus1.subsurface(12,0,12,20)
        self.player.left1= gus1.subsurface(24,0,10,20)
        self.player.right1 = gus1.subsurface(34,0,10,20)
        self.player.front2 = gus2.subsurface(0,0,12,20)
        self.player.back2 = gus2.subsurface(12,0,12,20)
        self.player.left2= gus2.subsurface(24,0,10,20)
        self.player.right2 = gus2.subsurface(34,0,10,20)

     

        #Initial attributes
        self.health = 100 #percent
        self.hunger = 0
        self.alive = True
        self.starving = False
        self.encumbrance = 0
        self.stamina = 100
        self.exhausted = False
        self.basespeed = 2
        self.inventory = []
        self.moving = False
        self.player.image = self.player.front
        self.dir = 0
        self.FRAMERATE = 10
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)
        self.running = False
        self.lastleft = self.player.left1
        self.lastright = self.player.right1
        self.lastback = self.player.back1
        self.lastfront = self.player.front1
        

    def updateHunger(self):
        if self.hunger < 100:
            if self.stamina < 25:
                self.hunger += 4
            self.hunger += 1
        else:
            self.starving = True
            print("starving")
            print(self.health)

    def updateStamina(self):
        if self.moving == True:
            staminaloss = .01+(self.encumbrance%25)*.01
            if self.running:
                staminaloss *= 5
                self.running = False
            if self.stamina > -5:
                self.stamina -= staminaloss
            if self.stamina < 0:
                self.exhausted = True
            self.moving = False
        else:
            if self.stamina < 100:
                self.stamina += .10
            if self.stamina > 0:
                #adjusts position, so coord is always even(Otherwise getting through
                #tight spaces gets difficult.
                if self.player.rect.x % 2 != 0:
                    self.player.rect.x += 1
                if self.player.rect.y % 2 != 0:
                    self.player.rect.y += 1
                self.exhausted = False

    def movePlayer(self,direction):
        lastimage = self.player.image
        SPEED = self.basespeed
        if self.running:
            SPEED *= 2
            self.FRAMERATE = 5
        else:
            self.FRAMERATE = 10
        if pygame.sprite.spritecollideany(self.player,setup.longgrass) != None\
        or self.exhausted: 
            self.running = False
            SPEED = 1
     
        VIEWDISTANCE = 150
        GUIWIDTH = 200
        self.moving = True

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                self.dir = 1
                SPEED *= -1
                
                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.left1:
                        self.lastleft = self.player.image  = self.player.left2                     
                    else:
                        self.lastleft = self.player.image = self.player.left1
                else:
                    self.player.image  = self.lastleft

            else:
                self.dir = 3
                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.right1:
                        self.lastright = self.player.image  = self.player.right2                     
                    else:
                        self.lastright = self.player.image = self.player.right1
                else:
                    self.player.image  = self.lastright
            
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

        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                self.dir = 1
                SPEED *= -1

                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.back1:
                        self.lastback = self.player.image  = self.player.back2                     
                    else:
                        self.lastback = self.player.image = self.player.back1
                else:
                    self.player.image  = self.lastback

            else:
                self.dir = 0

                if setup.frame % self.FRAMERATE == 0:
                    if self.player.image == self.player.front1:
                        self.lastfront = self.player.image  = self.player.front2                     
                    else:
                        self.lastfront = self.player.image = self.player.front1
                else:
                    self.player.image  = self.lastfront

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



    def updatePlayer(self):

        #Takes roughly 4 min. from full health to death when starving.
        self.updateStamina()
            
        if self.starving:
            self.health -= .1
        if self.health <= 0:
            self.alive = False
            
