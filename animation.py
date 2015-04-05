import setup,player
def handleAnimation(spr,dir):

    if setup.frame % setup.FRAMERATE == 0:

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