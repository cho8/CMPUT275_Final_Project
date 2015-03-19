import sys,pygame
from player import Player
from pygame import Surface
from pygame import sprite


PLAYERFRONT = "Gus_Front1.png"
PLAYERFRONT2 = "Gus_Front2.png"
PLAYERBACK = "Gus_Back1.png"
PLAYERLEFT = "Gus_Left.png"
PLAYERRIGHT = "Gus_Right.png"
CABIN = "Cabin.png"

screen = pygame.display.set_mode((400,400))
pygame.init()
back_x = 0
back_y = 0
background = pygame.image.load("gamemap.png").convert()
px = 20
py = 20
cabin = sprite.Sprite()
cabin.image = pygame.image.load(CABIN).convert_alpha()
cabin.rect = cabin.image.get_rect()
cabin.rect.x = 50
cabin.rect.y = 50
buildings = sprite.Group()
buildings.add(cabin)
player = Player(px,py,PLAYERFRONT,PLAYERFRONT2,PLAYERBACK,PLAYERLEFT,PLAYERRIGHT)
group = sprite.Group()
group.add(player)
clock = pygame.time.Clock
buildings.draw(background)
screen.blit(background, (back_x,back_y))
    
while 1:
    group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            keyup = False
            while keyup == False:
                
                player.move("RIGHT",group,buildings,screen,background)
                if player.rect.x + player.rect.width >= screen.get_width():
                    player.rect.x = screen.get_width() - player.rect.width
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
                player.move("DOWN",group,buildings,screen,background)                 
                if player.rect.y + player.rect.height >= screen.get_height():
                    player.rect.y = screen.get_height() - player.rect.height
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
                
                player.move("LEFT",group,buildings,screen,background)
                screen.blit(background, (back_x,back_y))
                if player.rect.x <= 0:
                    player.rect.x = 0
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
                
                player.move("UP",group,buildings,screen,background)
                screen.blit(background, (back_x,back_y))
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        keyup = True
    pygame.display.flip()

   
    