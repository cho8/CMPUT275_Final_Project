import sys,pygame
from player import Player
from pygame import Surface
from pygame import sprite


PLAYERFRONT = "images/Gus_Front1.png"
PLAYERFRONT2 = "images/Gus_Front2.png"
PLAYERBACK = "images/Gus_Back1.png"
PLAYERLEFT = "images/Gus_Left.png"
PLAYERRIGHT = "images/Gus_Right.png"
CABIN = "images/Cabin.png"

screen = pygame.display.set_mode((400,400))
pygame.init()
back_x = 0
back_y = 0
background = pygame.image.load("images/gamemap.png").convert()
px = 20
py = 20
cabin = sprite.Sprite()
cabin.image = pygame.image.load(CABIN).convert_alpha()
cabin.rect = cabin.image.get_rect()
cabin.rect.x = back_x + 50
cabin.rect.y = back_y + 50
buildings = sprite.Group()
buildings.add(cabin)
player = Player(px,py,PLAYERFRONT,PLAYERFRONT2,PLAYERBACK,PLAYERLEFT,PLAYERRIGHT)
clock = pygame.time.Clock
buildings.draw(background)
screen.blit(background, (back_x,back_y))
    
while 1:
    player.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            keyup = False
            while keyup == False:
                
                player.move("RIGHT",buildings,screen,background)
                if player.player.rect.x + player.player.rect.width >= screen.get_width():
                    player.player.rect.x = screen.get_width() - player.player.rect.width
                    back_x -= 2
                    if back_x < (0-(background.get_width()-screen.get_width())):
                        print("entered")
                        back_x = (0-(background.get_width()-screen.get_width()))
                screen.blit(background, (back_x,back_y))


                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        keyup = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            keyup = False
            while keyup == False:
                print(background.get_height())
                print(back_y)
                player.move("DOWN",buildings,screen,background)                 
                if player.player.rect.y + player.player.rect.height >= screen.get_height():
                    player.player.rect.y = screen.get_height() - player.player.rect.height
                    back_y -= 2
                if back_y < (0-(background.get_height()-screen.get_height())):
                    print("entered")
                    back_y = (0-(background.get_height()-screen.get_height()))
                screen.blit(background, (back_x,back_y))
                screen.blit(background, (back_x,back_y))

                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        keyup = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            keyup = False
            while keyup == False:
                
                player.move("LEFT",buildings,screen,background)
                screen.blit(background, (back_x,back_y))
                if player.player.rect.x <= 0:
                    player.player.rect.x = 0
                    back_x += 2
                    if back_x > 0:
                        back_x = 0
                screen.blit(background, (back_x,back_y))
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP or (event.type == pygame.KEYDOWN and event.key != pygame.K_a):
                        keyup = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            keyup = False
            while keyup == False:
                
                player.move("UP",buildings,screen,background)
                screen.blit(background, (back_x,back_y))
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        keyup = True
    pygame.display.flip()

   
    