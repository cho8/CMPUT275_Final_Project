import pygame,setup
from pygame.sprite import Group


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None, imagemap=None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        self.player.x_pos = x_pos
        self.player.y_pos = y_pos
        imagemap = pygame.image.load(imagemap).convert_alpha()
        self.player.front = imagemap.subsurface(0,0,12,20)
        self.player.back = imagemap.subsurface(12,0,12,20)
        self.player.left= imagemap.subsurface(24,0,10,20)
        self.player.right = imagemap.subsurface(34,0,10,20)
     

        #Initial attributes
        self.health = 100 #percent
        self.hunger = 0
        self.alive = True
        self.starving = False
        self.encumbrance = 0
        self.stamina = 100
        self.exhausted = False
        self.speed = 5
        self.stats = "Health:{} Stamina:{} Hunger:{} Starving:{} Speed:{}".format\
        (self.health,self.stamina,self.hunger,self.starving,self.speed)

        self.player.image = self.player.front
        self.player.rect = self.player.front.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)

    def updateHunger(self):
        if self.hunger < 100:
            self.hunger += 1
        else:
            self.starving = True
            print("starving")
            print(self.health)
    def updateStamina(self):
        if self.stamina > 0:
            self.stamina -= 1+(self.encumbrance%25)
        else:
            self.exhausted = True
    def movePlayer(self,direction):
        SPEED = self.speed
        VIEWDISTANCE = 150
        GUIWIDTH = 200

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                SPEED *= -1
                self.player.image = self.player.left
            else:
                self.player.image = self.player.right
            
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

            elif self.player.rect.x > setup.screen.get_width()-VIEWDISTANCE-GUIWIDTH:
                if setup.gui.bgx >(0-setup.background.get_width()+setup.screen.get_width()-GUIWIDTH):
                    self.player.rect.x = setup.screen.get_width()-VIEWDISTANCE-GUIWIDTH
                    setup.gui.bgx -= SPEED
                
                    for rect in setup.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED
                    for item in setup.items:
                        item.rect.x -= SPEED

            self.player.rect.x += SPEED

            if pygame.sprite.spritecollideany(self.player,setup.buildings) != None\
            or pygame.sprite.spritecollideany(self.player,setup.npcs) != None\
            or pygame.sprite.spritecollideany(self.player,setup.items) != None:

                self.player.rect.x -= SPEED

        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                SPEED *= -1
                self.player.image = self.player.back
            else:
                self.player.image = self.player.front

            if self.player.rect.y > setup.screen.get_height() - VIEWDISTANCE: 
                if setup.gui.bgy >(0-setup.background.get_height()+setup.screen.get_height()):
                    self.player.rect.y = setup.screen.get_height()-VIEWDISTANCE         
                    setup.gui.bgy -= SPEED
                    
                    for rect in setup.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED
                    for item in setup.items:
                        item.rect.y -= SPEED
            
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

            self.player.rect.y += SPEED

            if pygame.sprite.spritecollideany(self.player,setup.buildings) != None\
            or pygame.sprite.spritecollideany(self.player,setup.npcs) != None\
            or pygame.sprite.spritecollideany(self.player,setup.items) != None:

                self.player.rect.y -= SPEED


    def updatePlayer(self):
        #Takes roughly 4 min. from full health to death when starving.
        if self.starving:
            self.health -= .1
        if self.health <= 0:
            self.alive = False
        if self.exhausted:
            self.speed = 1
            
