import pygame

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    """
    Draw some text into an area of a surface.
    Automatically wraps words.
    Returns any text that didn't get blitted.
    
    The base code for this function is sourced from http://www.pygame.org/wiki/TextWrap
    but is modified for the use in our project
    """
    y = rect.top
    lineSpacing = -2
 
    # get the height of the font
    fontHeight = font.size("s")[1]
    fontWidth = font.size("s")[0]
    lineLength = fontWidth
 
    while text:
        i = 1
 
        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            pass

        # determine maximum width of line
        while lineLength < rect.w and i < len(text):
            lineLength += fontWidth
            i += 1
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text):
            lineLength = text.rfind(" ", 0, i) + 1
        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:lineLength], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:lineLength], aa, color)
 
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
 
        # remove the text we just blitted
        text = text[lineLength:]
 
    return text