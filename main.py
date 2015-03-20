import sys,pygame
from setup import Setup
from player import Player
from pygame import sprite

clock = pygame.time.Clock

player = Player(Setup.pstart_x,Setup.pstart_y,\
Setup.PLAYERFRONT,Setup.PLAYERFRONT2,Setup.PLAYERBACK,\
Setup.PLAYERLEFT,Setup.PLAYERRIGHT)
    
while 1:
    player.draw(Setup.screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            keyup = False
            while keyup == False:
                
                player.move("RIGHT",Setup.background)
               


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

   
    