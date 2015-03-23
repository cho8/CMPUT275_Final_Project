import sys, pygame
from pygame.sprite import LayeredUpdates
from collections import namedtuple
import item

# GUI size things
RESOLUTION = pygame.Rect(0,0, 600,400)
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 80
BAR_WIDTH = 200
MAP_WIDTH = 400
PAD = 4

# Set fonts
pygame.font.init()
FONT_SIZE = 16
BIG_FONT_SIZE = 42
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
FONT_COLOUR = (0, 0, 0)

# Colour stuff
GUI_COLOUR = (150, 150, 150)
OUTLINE_COLOUR = (50, 50, 50)
BUTTON_HIGHLIGHT_COLOUR = (255, 255, 255)
BUTTON_DISABLED_COLOUR = (64, 64, 64)

# A container class which stores button information.
# slot_height and slot_width represents the number of BUTTON_HEIGHT and BUTTON WIDTH of the button relative to the bottom and right edge of gui.
Button = namedtuple('Button', ['slot_height', 'slot_width', 'text', 'onClick', 'condition'])

class GUI(LayeredUpdates):
    num_instances = 0

    def __init__(self, screen_rect):
        """
        Initialized display.
        """

        LayeredUpdates.__init__(self)

        if GUI.num_instances != 0:
            raise Exception("GUI: can only have one instance of a simulation")
        num_instances = 1

        #setup screen
        self.screen = pygame.display.set_mode((screen_rect.w, screen_rect.h))
        self.screen_rect = RESOLUTION

        #rect for gui bar
        self.gui_rect = pygame.Rect(RESOLUTION.w - BAR_WIDTH,
                                    0,
                                    BAR_WIDTH,
                                    RESOLUTION.h)

        #rect for play area
        self.view_rect = pygame.Rect(0,
                                    0,
                                    MAP_WIDTH,
                                    screen_rect.h)

        self.map = pygame.image.load("images/gamemap_test.png").convert()

        #Set up GUI
        self.buttons = [
            Button(1, 1, "USE", self.use_pressed, self.item_selected),
            Button(1, 0, "DISCARD", self.discard_pressed, self.item_selected),
            Button(0, 0, "SEARCH", self.search_pressed, None),
            Button(0, 1, "AUTO-EAT", self.auto_pressed, None)]
        
        #Currently Selected Item in Inventory
        self.sel_item = None

    def use_pressed(self):
        if self.sel_item == None:
            return
        #if the item is usable, consume it and remove it from inventory
        self.sel_item.consume_item()
        self.sel_item = None

    def discard_pressed(self):
        if self.sel_item == None:
            return
        self.sel_item.discard()
        self.sel_item = None

    def search_pressed():
        """
        Search for usable items on the current and adjacent tiles of the player.
        """
        #Gotta figure out the player/map stuff first
        pass

    def auto_pressed(self):
        """
        Calls auto-use function based on which stat is selected.
        Optimally consumes the items that restores the most hunger 
        and relieves the most inventory space
        """
        
        # Leaving the memoization part for later
        pass
    
    def item_selected(self):
        """
        An item in the inventory is clicked/selected
        """
        pass

    def draw(self):
        """
        Render display.
        """
        LayeredUpdates.draw(self, self.screen)
        self.screen.blit(self.map, (0,0))

        #draw player
        #draw collisions
        #draw items
        #draw npcs

    def draw_gui(self):
        """
        Draws the interface on the right side of the screen.
        """

#        if not self.map: return

        line_num = 0
        # determine mouse position
        mouse_pos = pygame.mouse.get_pos()
        #coords = self.map.tile_coords(mouse_pos)

        # draw gui background
        guiRect = self.gui_rect
        pygame.draw.rect(self.screen, GUI_COLOUR, guiRect)

        # draw outline of gui
        outlineRect = self.gui_rect.copy()
        outlineRect.w -= 1
        outlineRect.h -= 1
        
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, outlineRect, 2)

        # display player stats
        player_name = FONT.render("Gus", True, FONT_COLOUR)
        self.screen.blit(player_name,
                         (self.gui_rect.centerx - (player_name.get_width()/2),
                          FONT_SIZE*line_num))

        # update screen
        pygame.display.flip()

screen = pygame.display.set_mode((600,400))
pygame.init()
background = pygame.image.load("images/gamemap_test.png").convert()
main_gui = GUI(RESOLUTION)
while 1:
    main_gui.draw()
    main_gui.draw_gui()
    screen.blit(background, (0,0))




                                 


