from setup import Setup
import pygame
from pygame.sprite import Group


class Player(Group):
    def __init__(self, x_pos=None, y_pos=None, imagefile1=None, imagefile2=None, imagefile3 = None,imagefile4 = None,imagefile5 = None):

        Group.__init__(self)        

        self.player = pygame.sprite.Sprite()
        self.player.x_pos = x_pos
        self.player.y_pos = y_pos
        self.player.imagefile1 = imagefile1
        self.player.imagefile2 = imagefile2
        self.player.imagefile3 = imagefile3
        self.player.imagefile4 = imagefile4
        self.player.imagefile5 = imagefile5
     

        #Put initial attributes here




        #
        self.player.image1 = pygame.image.load(imagefile1).convert_alpha()
        self.player.image2 = pygame.image.load(imagefile2).convert_alpha()
        self.player.image3 = pygame.image.load(imagefile3).convert_alpha()
        self.player.image4 = pygame.image.load(imagefile4).convert_alpha()
        self.player.image5 = pygame.image.load(imagefile5).convert_alpha()
        self.player.image = self.player.image1
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = x_pos
        self.player.rect.y = x_pos
        self.add(self.player)
        print("reset")

    def move(self,direction):
        speed = 2
        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                speed *= -1
                self.player.image = self.player.image4
            else:
                self.player.image = self.player.image5
            if self.player.rect.x + self.player.rect.width >= Setup.screen.get_width():
                self.player.rect.x = screen.get_width() - self.player.rect.width
                back_x -= 2
                if back_x < (0-(Setup.background.get_width()-Setup.screen.get_width())):
                    print("entered")
                    Setup.back_x = (0-(Setup.background.get_width()-\
                    Setup.screen.get_width()))
                screen.blit(Setup.background, (Setup.back_x,Setup.back_y))
            if pygame.sprite.spritecollideany(self.player,Setup.buildings) != None:
                if direction == "LEFT":
                    self.player.rect.x += 1
                elif direction == "RIGHT":
                    self.player.rect.x -= 1
                else:
                    self.player.rect.x += speed
            
        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                speed *= -1
                self.player.image = self.player.image3
            else:
                self.player.image = self.player.image1
            if pygame.sprite.spritecollideany(self.player,buildings) != None:
                if direction == "UP":
                    self.player.rect.y += 1
                else:
                    self.player.rect.y -= 1
            else:
                self.player.rect.y += speed

        
        self.clear(Setup.screen,background)
        self.draw(Setup.screen)
        pygame.display.update(self.player.rect)


