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
 

    def move(self,direction,group):
        SPEED = 2

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                SPEED *= -1
                group.player.image = group.player.image4
            else:
                group.player.image = group.player.image5

            if group.player.rect.x + group.player.rect.width >= self.screen.get_width():
                group.player.rect.x = self.screen.get_width() - group.player.rect.width
                self.bgx -= SPEED
                if self.bgx < (0-(self.background.get_width()-self.screen.get_width())):
                    self.bgx = (0-(self.background.get_width()-self.screen.get_width()))
                self.update()
            elif group.player.rect.x < 0:
                group.player.rect.x = 0
                self.update()
                return

            if pygame.sprite.spritecollideany(group.player,setup.buildings) != None:
                if direction == "LEFT":
                    group.player.rect.x += 1
                elif direction == "RIGHT":
                    group.player.rect.x -= 1
                return

            group.player.rect.x += SPEED
         
        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                SPEED *= -1
                group.player.image = group.player.image3
            else:
                group.player.image = group.player.image1

            if group.player.rect.y + group.player.rect.height >= self.screen.get_height():
                group.player.rect.y = self.screen.get_height() - group.player.rect.height
                self.bgy -= SPEED
                if self.bgy < (0-(self.background.get_height()-self.screen.get_height())):
                    self.bgy = (0-(self.background.get_height()-self.screen.get_height()))
                self.update()
            elif group.player.rect.y < 0:
                group.player.rect.y = 0
                return
            if pygame.sprite.spritecollideany(group.player,setup.buildings) != None:
                if direction == "UP":
                    group.player.rect.y += 1
                elif direction == "DOWN":
                    group.player.rect.y -= 1
                return
         
            group.player.rect.y += SPEED

        
        group.clear(self.screen,self.background)
        group.draw(self.screen)

    def update(self):
        pygame.display.flip()
        self.screen.blit(self.background,(self.bgx,self.bgy))
        self.player.draw(self.screen)
        self.buildings.draw(self.background)