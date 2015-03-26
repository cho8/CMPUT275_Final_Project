import pygame
import setup

class GUI():

    def __init__(self):
        self.screen = setup.screen
        self.background = setup.background
        background = setup.background
        self.bgx = setup.bgx
        self.bgy = setup.bgy
        self.player = setup.player
        self.buildings = setup.buildings
 
    def movePlayer(self,direction,group):
        SPEED = setup.player_speed
        VIEWDISTANCE = 150

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                SPEED *= -1
                group.player.image = group.player.left
            else:
                group.player.image = group.player.right
            
            if group.player.rect.x < VIEWDISTANCE:               
                if self.bgx < 0:
                    group.player.rect.x = VIEWDISTANCE
                    self.bgx -= SPEED
                    
                    for rect in self.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED

            elif group.player.rect.x > self.screen.get_width()-VIEWDISTANCE:
                if self.bgx >(0-self.background.get_width()+self.screen.get_width()):
                    group.player.rect.x = self.screen.get_width()-VIEWDISTANCE
                    self.bgx -= SPEED
                
                    for rect in self.buildings:
                        rect.rect.x -= SPEED
                    for spr in setup.npcs:
                        spr.rect.x -= SPEED

            group.player.rect.x += SPEED

            if pygame.sprite.spritecollideany(group.player,setup.buildings) != None:

                group.player.rect.x -= SPEED

        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                SPEED *= -1
                group.player.image = group.player.back
            else:
                group.player.image = group.player.front

            if group.player.rect.y > self.screen.get_height() - VIEWDISTANCE: 
                if self.bgy >(0-self.background.get_height()+self.screen.get_height()):
                    group.player.rect.y = self.screen.get_height()-VIEWDISTANCE         
                    self.bgy -= SPEED
                    
                    for rect in self.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED
            
            elif group.player.rect.y < VIEWDISTANCE:
                if self.bgy < 0:
                    group.player.rect.y = VIEWDISTANCE
                    self.bgy -= SPEED
                
                    for rect in self.buildings:
                        rect.rect.y -= SPEED
                    for spr in setup.npcs:
                        spr.rect.y -= SPEED

            group.player.rect.y += SPEED

            if pygame.sprite.spritecollideany(group.player,setup.buildings) != None:

                group.player.rect.y -= SPEED

    def update(self):
        pygame.display.flip()
        self.screen.blit(self.background,(self.bgx,self.bgy))
        self.player.draw(self.screen)
        self.buildings.draw(self.screen)
        setup.npcs.draw(self.screen)