import pygame
import setup
import item
from collections import namedtuple

# GUI size things
RESOLUTION_RECT = pygame.Rect(0,0, 600,400)
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 100
GUI_WIDTH = 200
MAP_WIDTH = 400
BAR_WIDTH = 100
PAD = 5

# Set fonts
pygame.font.init()
SMALL_FONT_SIZE = 14
FONT_SIZE = 16
BIG_FONT_SIZE = 18
SMALL_FONT = pygame.font.SysFont("Arial", SMALL_FONT_SIZE)
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
FONT_COLOUR = (0, 0, 0)

# Colour stuff
GUI_COLOUR = (150, 150, 150)
OUTLINE_COLOUR = (255, 255, 255)
BUTTON_HIGHLIGHT_COLOUR = (255, 255, 255)
BUTTON_DISABLED_COLOUR = (64, 64, 64)
RED_BAR = (255,0,0)
GREEN_BAR = (0,255,0)


# A container class which stores button information.
# slot_height and slot_width represents the number of BUTTON_HEIGHT and BUTTON WIDTH of the button relative to the bottom and right edge of gui.
Button = namedtuple('Button', ['slot_x', 'slot_y', 'text', 'onClick', 'condition'])

class GUI():
    
    num_instances = 0
    def __init__(self):
        
        if GUI.num_instances != 0:
            raise Exception("GUIL can only have one instance of a simulation")
        num_instance = 1
        
        self.screen = setup.screen
        self.screen_rect = RESOLUTION_RECT
                                    
        self.background = setup.background
        self.bgx = setup.bgx
        self.bgy = setup.bgy
        self.player = setup.player
        self.buildings = setup.buildings
        self.items = setup.items
    
    
        #rect for gui
        self.gui_rect = pygame.Rect(RESOLUTION_RECT.w - GUI_WIDTH,
                                    0,
                                    GUI_WIDTH,
                                    RESOLUTION_RECT.h)

        #rect for play area
        self.play_rect = pygame.Rect(0,
                                    0,
                                    MAP_WIDTH,
                                    self.screen_rect.h)
                                    
        #Set up GUI
        self.buttons = [
            Button(1, 1, "USE", self.use_pressed, self.item_selected),
            Button(0, 1, "DISCARD", self.discard_pressed, self.item_selected),
            Button(0, 0, "SEARCH", self.search_pressed, None),
            Button(1, 0, "AUTO-EAT", self.auto_pressed, None)]
    
        #Currently Selected Item in Inventory
        self.sel_item = None
    
    def draw_gui(self):
        """
        Draws the interface on the right side of the screen.
        """
        if not self.background: return
    
        line_num = 0
        # determine mouse position
        mouse_pos = pygame.mouse.get_pos()
        #coords = self.map.tile_coords(mouse_pos)

        # draw gui background
        guiRect = self.gui_rect
        pygame.draw.rect(self.screen, GUI_COLOUR, guiRect)

        # draw outline of gui
        outline_rect = self.gui_rect.copy()
        outline_rect.w -= 1
        outline_rect.h -= 1
        
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, outline_rect, 2)
        
        #rect for stats bars
        bar_gen_rect = pygame.Rect(0,
                                    0,
                                    BAR_WIDTH,
                                    FONT_SIZE - PAD)

        # display player stats
        player_name = BIG_FONT.render("Gus", True, FONT_COLOUR)
        self.screen.blit(player_name,
                         (self.gui_rect.centerx - (player_name.get_width()/2),
                          FONT_SIZE*line_num + PAD))
        line_num += 1
        
        # health stat
        player_health = FONT.render("Health", True, FONT_COLOUR)
        self.screen.blit(player_health,
                         (self.gui_rect.left + PAD,
                          FONT_SIZE*line_num + PAD))

        health_rect = bar_gen_rect.copy()
        health_rect.x, health_rect.y = RESOLUTION_RECT.w - (self.gui_rect.w)/2 - PAD, \
                                        BIG_FONT_SIZE*line_num + 1.3*PAD
        health_rect.w = self.player.health
        # bar color
        bar_colour = RED_BAR if self.player.health <= 30 else GREEN_BAR
        pygame.draw.rect(self.screen, bar_colour, health_rect)
        line_num += 1
        
        # hunger stat
        player_hunger = FONT.render("Hunger", True, FONT_COLOUR)
        self.screen.blit(player_hunger,
                         (self.gui_rect.left + PAD,
                          FONT_SIZE*line_num + PAD))
        hunger_rect = bar_gen_rect.copy()
        hunger_rect.x, hunger_rect.y = RESOLUTION_RECT.w - (self.gui_rect.w)/2 - PAD, \
                                        FONT_SIZE*line_num + 2*PAD
        hunger_rect.w = self.player.hunger
        bar_colour  = RED_BAR if self.player.hunger >= 70 else GREEN_BAR
        pygame.draw.rect(self.screen, bar_colour, hunger_rect)
        line_num += 1
        
        # stamina stat
        player_stamina = FONT.render("Stamina", True, FONT_COLOUR)
        self.screen.blit(player_stamina,
                         (self.gui_rect.left + PAD,
                          FONT_SIZE*line_num + PAD))
        stamina_rect = bar_gen_rect.copy()
        stamina_rect.x, stamina_rect.y = RESOLUTION_RECT.w - \
                                        (self.gui_rect.w)/2 - PAD,\
                                        FONT_SIZE*line_num + 2*PAD
        stamina_rect.w = self.player.stamina
        bar_colour = RED_BAR if self.player.stamina <= 30 else GREEN_BAR
        pygame.draw.rect(self.screen,bar_colour, stamina_rect)
        line_num += 2
        
        #divider
        pygame.draw.line(self.screen, OUTLINE_COLOUR, (self.gui_rect.left, FONT_SIZE*line_num), (self.gui_rect.right, FONT_SIZE*line_num))
        
        #inventory box
        self.draw_inventory_list(self.player.inventory)

        #buttons
        for button in self.buttons:
            self.draw_gui_button(button)
        
    def draw_inventory_list(self, inventory):
        """
        Draws the list of items (inventory) into the gui
        """
        inventory_rect = self.gui_rect.copy()
        inventory_rect.x += 5
        inventory_rect.y += 84
        inventory_rect.w -= 10
        inventory_rect.h -= 180
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, inventory_rect, 1)
        for item in self.player.inventory:
            item.list_rect = inventory_rect.copy()
            item.list_rect.h = item.list_rect.h/8
            item_name = FONT.rend(item.name, True, FONT_COLOUR)
            self.screen.blit(item_name,
                            (inventoryRect + PAD,
                            FONT_SIZE*line_num+PAD))

    def draw_gui_button(self, button):
        """
        Renders a button to the bar.
        If the mouse is hovering over the button it is rendered in white,
        else rgb(50, 50, 50).
        """
        but_x = self.screen_rect.w - (self.gui_rect.w/2)*(button.slot_x+1) + PAD
        but_y = self.screen_rect.h - (self.gui_rect.h/9)*(button.slot_y+1) 
        but_rect = pygame.Rect(but_x,
                                but_y,
                                BUTTON_WIDTH,
                                BUTTON_HEIGHT)
        
        # The outline needs a slightly smaller rectangle
        but_out_rect = but_rect
        but_out_rect.width -= 10

        # Determine the button color
        but_colour = GUI_COLOUR
        
        # The button can't be used
        if button.condition and not button.condition():
            but_colour = BUTTON_DISABLED_COLOUR
        else:
            # The button can be used
            mouse_pos = pygame.mouse.get_pos()
            if but_rect.collidepoint(mouse_pos):
                # Highlight on mouse over
                but_colour = BUTTON_HIGHLIGHT_COLOUR
        
        # Draw the button
        pygame.draw.rect(self.screen, but_colour, but_rect)
            
        # Draw the outline
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, but_out_rect, 2)

        # Draw the text
        but_text = FONT.render(button.text, True, FONT_COLOUR)
        self.screen.blit(
            but_text,
            (but_rect.centerx - (but_text.get_width()/2),
            but_rect.y + (BUTTON_HEIGHT//2) - but_text.get_height()//2))
    
    def use_pressed(self):
        """
        Use button is clicked while an inventory item is selected.
        """
        if self.sel_item == None:
            return
        #if the item is usable, consume it and remove it from inventory
        self.sel_item.consume_item()
        self.sel_item = None

    def discard_pressed(self):
        """
        Discard button is clicked while an inventory item is selected.
        """
        if self.sel_item == None:
            return
        self.sel_item.discard(self.player.inventory)
        self.sel_item = None

    def search_pressed():
        """
        Search for usable items on the current and adjacent positions of the player
        """
        #check collision between player and any item
        eligible_item = pygame.sprite.spritecollideany(self.player,setup.items)
        if eligible_tem:
            eligible_item.pick_up(self.player.inventory)
            self.item
    

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
        An item in the inventory is clicked/selected. Returns true or false.
        """
        if self.sel_unit: return True
        else: return False
    
    
    def on_click(self,e):
        """
        Handles clicking events.
        """
        if (e.type == pygame.MOUSTBUTTONUP
            and e.button ==1
            and pygame.mouse.get_focused()):
            
            # if the inside of the gui was clicked
            if self.gui_rect.collidepoint(e.pos):
                itm = get_item_at_point(e.pos)
            
                # if the click position is not on an item, check for button
                if not itm:
                    button_at_point(e.pos)

    def get_item_at_point(self,pos):
        """
        Returns the item if the click position is within its rect
        """
        for i in self.player.inventory:
            if i.list_rect.collidepoint(pos):
                self.sel_item = i
                return i
    
    def button_at_point(self,pos):
        """
        Detects if a button is pressed at the click position, if there is,
        perform its function when it is clicked.
        """
        for button in self.buttons:
            # If the button is enabled and clickable, call the click function
            if ((not button.condition or button.condition()) and
                self.get_button_rect(button).collidpoint(pos)):
                button.onClick()
    
   
    def update(self):
        self.screen.blit(self.background,(self.bgx,self.bgy))
        self.player.draw(self.screen)
        self.buildings.draw(self.screen)
        setup.items.draw(self.screen)
        setup.npcs.draw(self.screen)
        self.draw_gui()
        pygame.display.flip()