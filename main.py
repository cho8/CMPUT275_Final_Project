import sys,pygame,setup
from gui import GUI

pygame.init()
gui = GUI()
player = setup.player
clock = pygame.time.Clock
pygame.key.set_repeat(1)
    
while 1:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_d]:                
                gui.move("RIGHT",player)
           
            if keys[pygame.K_s]:
                gui.move("DOWN",player)

            if keys[pygame.K_a]:
                gui.move("LEFT",player)

            if keys[pygame.K_w]:
                gui.move("UP",player)

    gui.update()
    