import sys,pygame,setup,AI
from gui import GUI

pygame.init()
gui = setup.gui
player = setup.player
npcs = setup.npcs
clock = pygame.time.Clock()
pygame.key.set_repeat(1)
pygame.time.set_timer(setup.UPDATESTATUS,6000)#Ten minutes until starving
endscreen = pygame.Surface((setup.screen.get_width(),setup.screen.get_height()))
endscreen.fill(55)
while True:

    while player.alive:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_SPACE]:
                    player.player.running = True

                if keys[pygame.K_d]:
                    player.moving == True                
                    player.movePlayer("RIGHT")
           
                elif keys[pygame.K_s]:
                    player.moving == True
                    player.movePlayer("DOWN")

                elif keys[pygame.K_a]:
                    player.moving == True
                    player.movePlayer("LEFT")

                elif keys[pygame.K_w]:
                    player.moving == True
                    player.movePlayer("UP")

            elif event.type == pygame.MOUSEBUTTONUP:
                gui.on_click(event)

            if event.type == setup.UPDATESTATUS:
                print("Health:{} Stamina:{} Hunger:{} Starving:{} Encumbrance:{}".format\
        (player.health,player.stamina,player.hunger,player.starving,player.encumbrance))
                player.updateHunger()            
    
        clock.tick(30)
        setup.frame +=1
        AI.updateNPC(npcs)
        player.updatePlayer()    
        gui.update()


    endscreen = pygame.Surface((gui.screen.get_width(),\
    gui.screen.get_height()),pygame.SRCALPHA)

    alpha = 0
    while alpha < 255:
        pygame.time.delay(100)
        alpha += 5
        endscreen.fill((0,0,0,alpha))
        gui.screen.blit(endscreen,(0,0))
        print(endscreen.get_alpha())
        pygame.display.flip()



    