import sys,pygame,setup,AI,animation, item.fire
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
time = 0

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
            elif keys[pygame.K_k]:
                player.alive = False

        elif event.type == pygame.MOUSEBUTTONUP:
            gui.on_click(event)

        if event.type == setup.UPDATESTATUS:
            print("Health:{} Stamina:{} Hunger:{} Starving:{} Encumbrance:{}".format\
        (player.health,player.stamina,player.hunger,player.starving,player.encumbrance))
            player.updateHunger()
            time += 6
            gui.update_timer()
            #update fire
            for i in setup.items:
                if i.name == "Fire":
                    i.timer += 1
                    if i.timer >= 5:
                        setup.items.remove(i)
    
    
    
    clock.tick(30)
    setup.frame +=1
    AI.updateNPC(npcs)
    player.updatePlayer()    
    gui.update()


endscreen = pygame.Surface((gui.screen.get_width(),\
gui.screen.get_height()),pygame.SRCALPHA)

gui.killPlayer()

alpha = 0
while alpha < 100:
    pygame.time.delay(50)
    alpha += 5
    endscreen.fill((0,0,0,alpha))
    gui.screen.blit(endscreen,(0,0))
    print(endscreen.get_alpha())
    pygame.display.flip()
message = "You survived for {} minutes!".format(time/60)
FONT = pygame.font.SysFont("Arial", 32)
endmsg = FONT.render(message,True,(255,0,0,alpha),pygame.SRCALPHA)

gui.screen.blit(endmsg,(100,(gui.screen.get_height()/2)-32))
pygame.display.flip()
 
#rect = pygame.Rect(endgame.get_width()/2-32,endgame.get_height()/2-100,32,100)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()


    