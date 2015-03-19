from pygame.sprite import Sprite
import pygame

class Player(Sprite):

    def __init__(self, x_pos=None, y_pos=None, imagefile1=None, imagefile2=None, imagefile3 = None,imagefile4 = None,imagefile5 = None):

        Sprite.__init__(self)        

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.imagefile1 = imagefile1
        self.imagefile2 = imagefile2
        self.imagefile3 = imagefile3
        self.imagefile4 = imagefile4
        self.imagefile5 = imagefile5
     

        #Put initial attributes here




        #
        self.image1 = pygame.image.load(imagefile1).convert_alpha()
        self.image2 = pygame.image.load(imagefile2).convert_alpha()
        self.image3 = pygame.image.load(imagefile3).convert_alpha()
        self.image4 = pygame.image.load(imagefile4).convert_alpha()
        self.image5 = pygame.image.load(imagefile5).convert_alpha()
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        print("reset")

    def move(self,direction,group,buildings,screen,background):
        speed = 2
        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                speed *= -1
                self.image = self.image4
            else:
                self.image = self.image5
            if pygame.sprite.spritecollideany(self,buildings) != None:
                if direction == "LEFT":
                    self.rect.x += 1
                else:
                    self.rect.x -= 1
            else:
                self.rect.x += speed
            
        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                speed *= -1
                self.image = self.image3
            else:
                self.image = self.image1
            if pygame.sprite.spritecollideany(self,buildings) != None:
                if direction == "UP":
                    self.rect.y += 1
                else:
                    self.rect.y -= 1
            else:
                self.rect.y += speed

        
        group.clear(screen,background)
        group.draw(screen)
        pygame.display.update(self.rect)


