import sys,pygame,setup
from gui import GUI

pygame.init()
gui = GUI()
player = setup.player
clock = pygame.time.Clock()
pygame.key.set_repeat(1)
pygame.time.set_timer(setup.UPDATEHUNGER,6000)#Ten minutes until starving
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
                print(clock.get_time())

                if keys[pygame.K_d]:                
                    gui.movePlayer("RIGHT",player)
           
                if keys[pygame.K_s]:
                    gui.movePlayer("DOWN",player)

                if keys[pygame.K_a]:
                    gui.movePlayer("LEFT",player)

                if keys[pygame.K_w]:
                    gui.movePlayer("UP",player)
            elif event.type == setup.UPDATEHUNGER:
                player.updateHunger()
    
        clock.tick(40)

        gui.update()
        player.updatePlayer()
    surface = pygame.display.get_surface()
    alpha = 0
    while alpha < 255:
        surface.fill(1)
        print(endscreen.get_alpha())
        pygame.time.delay(100)
        alpha += 5
        surface.set_alpha(alpha)
        surface.blit(setup.screen,(0,0))
        pygame.display.flip()
    