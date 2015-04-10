import setup,player, pygame

def playerHurt(gui):

    hurtscreen = pygame.Surface((gui.screen.get_width(),\
    gui.screen.get_height()),pygame.SRCALPHA)


    alpha = 20
    while alpha > 0:
        pygame.time.delay(10)
        hurtscreen.fill((255,0,0,alpha))
        gui.screen.blit(hurtscreen,(0,0))
        pygame.display.flip()
        alpha -= 5
        
def handleAnimation(spr,dir):

    framerate = setup.FRAMERATE

    if spr.type == "Player" and spr.running:
        
        framerate /=2

    if setup.frame % framerate == 0:

        if dir == 1:

            if spr.image == spr.left1:
                spr.lastleft = spr.image  = spr.left2                     
            else:
                spr.lastleft = spr.image = spr.left1
        elif dir == 3:

            if spr.image == spr.right1:
                spr.lastright = spr.image  = spr.right2                     
            else:
                spr.lastright = spr.image = spr.right1
        elif dir == 0:

            if spr.image == spr.front1:
                spr.lastfront = spr.image  = spr.front2                     
            else:
                spr.lastfront = spr.image = spr.front1
        elif dir == 2:

            if spr.image == spr.back1:
                spr.lastback = spr.image  = spr.back2                     
            else:
                spr.lastback = spr.image = spr.back1
       
    else:
        if dir == 1:
           spr.image  = spr.lastleft
        elif dir == 3:
           spr.image  = spr.lastright
        elif dir == 0:
           spr.image  = spr.lastfront
        elif dir == 2:
           spr.image  = spr.lastback


    if spr.type is not "Player" and spr.type is not "Tool":
        spr.rect.size = spr.image.get_size()
