import pygame
import setup
from collections import namedtuple

# GUI size things
RESOLUTION_RECT = pygame.Rect(0,0, 600,400)
BUTTON_HEIGHT = 50
BUTTON_WIDTH = 80
BAR_WIDTH = 200
MAP_WIDTH = 400
PAD = 4

# Set fonts
pygame.font.init()
FONT_SIZE = 16
BIG_FONT_SIZE = 18
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
FONT_COLOUR = (0, 0, 0)

# Colour stuff
GUI_COLOUR = (150, 150, 150)
OUTLINE_COLOUR = (255, 255, 255)
BUTTON_HIGHLIGHT_COLOUR = (255, 255, 255)
BUTTON_DISABLED_COLOUR = (64, 64, 64)

# A container class which stores button information.
# slot_height and slot_width represents the number of BUTTON_HEIGHT and BUTTON WIDTH of the button relative to the bottom and right edge of gui.
Button = namedtuple('Button', ['slot_height', 'slot_width', 'text', 'onClick', 'condition'])

class GUI():
    
    num_instances = 0
    def __init__(self):
        
        if GUI.num_instances != 0:
            raise Exception("GUIL can only have one instance of a simulation")
        num_instance = 1
        
        self.screen = setup.screen
        self.screen_rect = RESOLUTION_RECT
                                    
        self.background = setup.background
        self.offscr_buildings = setup.offscr_buildings
        self.bgx = setup.bgx
        self.bgy = setup.bgy
        self.player = setup.player
        self.buildings = setup.buildings
    
        #rect for gui bar
        self.gui_rect = pygame.Rect(RESOLUTION_RECT.w - BAR_WIDTH,
                                    0,
                                    BAR_WIDTH,
                                    RESOLUTION_RECT.h)

        #rect for play area
        self.play_rect = pygame.Rect(0,
                                    0,
                                    MAP_WIDTH,
                                    self.screen_rect.h)
        #Set up GUI
        self.buttons = [
            Button(1, 1, "USE", self.use_pressed, self.item_selected),
            Button(1, 0, "DISCARD", self.discard_pressed, self.item_selected),
            Button(0, 0, "SEARCH", self.search_pressed, None),
            Button(0, 1, "AUTO-EAT", self.auto_pressed, None)]
    
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
        outlineRect = self.gui_rect.copy()
        outlineRect.w -= 1
        outlineRect.h -= 1
        
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, outlineRect, 2)

        # display player stats
        player_name = BIG_FONT.render("Gus", True, FONT_COLOUR)
        self.screen.blit(player_name,
                         (self.gui_rect.centerx - (player_name.get_width()/2),
                          BIG_FONT_SIZE*line_num + PAD))
        #update number or bar graphic
        line_num += 1
        player_health = FONT.render("Health", True, FONT_COLOUR)
        self.screen.blit(player_health,
                         (self.gui_rect.left + PAD,
                          FONT_SIZE*line_num + PAD))
        #update number or bar graphic
        line_num += 1
        player_hunger = FONT.render("Hunger", True, FONT_COLOUR)
        self.screen.blit(player_hunger,
                         (self.gui_rect.left + PAD,
                          FONT_SIZE*line_num + PAD))
        #update number or bar graphic
        line_num += 1
        player_stamina = FONT.render("Stamina", True, FONT_COLOUR)
        self.screen.blit(player_stamina,
                         (self.gui_rect.left + PAD,
                          FONT_SIZE*line_num + PAD))
        line_num += 2
        
        #divider
        pygame.draw.line(self.screen, OUTLINE_COLOUR, (self.gui_rect.left, FONT_SIZE*line_num), (self.gui_rect.right, FONT_SIZE*line_num))
        
        #inventory box
        
        #buttons

    def draw_gui_button(self, button, startpos):
        """
        Renders a button to the bar.
        If the mouse is hovering over the button it is rendered in white,
        else rgb(50, 50, 50).
        """
        
        # Gotta figure out the button rect dimensions
        #but_rect = pygame.Rect()
        
        # The outline needs a slightly smaller rectangle
        but_out_rect = but_rect
        but_out_rect.width -= 1

        # Determine the button color
        but_color = BAR_COLOR
        
        # The button can't be used
        if button.condition and not button.condition():
            but_color = BUTTON_DISABLED_COLOR
        else:
            # The button can be used
            mouse_pos = pygame.mouse.get_pos()
            if but_rect.collidepoint(mouse_pos):
                # Highlight on mouse over
                but_color = BUTTON_HIGHLIGHT_COLOR
        
        # Draw the button
        pygame.draw.rect(self.screen, but_color, but_rect)
            
        # Draw the outline
        pygame.draw.rect(self.screen, OUTLINE_COLOR, but_out_rect, 2)

        # Draw the text
        but_text = FONT.render(button.text, True, FONT_COLOR)
        self.screen.blit(
            but_text,
            (self.bar_rect.centerx - (but_text.get_width()/2),
            but_rect.y + (BUTTON_HEIGHT//2) - but_text.get_height()//2))
    
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
 

    def movePlayer(self,direction,group):
        SPEED = setup.player_speed
        

        if direction == "LEFT" or direction == "RIGHT":
            if direction == "LEFT":
                SPEED *= -1
                group.player.image = group.player.left
            else:
                group.player.image = group.player.right
               
            if group.player.rect.x < 0:
                group.player.rect.x = 0
                self.bgx -= SPEED
                if self.bgx > -25:
                    self.bgx = 0
                self.buildings.clear(self.screen,self.background)
                for rect in self.buildings:
                    rect.rect.x -= SPEED
                self.buildings.draw(self.screen)
                print(self.bgx)

            elif group.player.rect.x + group.player.rect.width >= self.play_rect.w:
                group.player.rect.x = self.play_rect.w - group.player.rect.width - PAD
                self.bgx -= SPEED
                
                if self.bgx < (0-(self.background.get_width()-self.play_rect.w)):
                    self.bgx = (0-(self.background.get_width()-self.play_rect.w))
                
                else:
                    self.buildings.clear(self.screen,self.background)
                    for rect in self.buildings:
                        if rect.rect.x + rect.rect.w >= self.play_rect.w:
                            self.buildings.remove(rect)
                            self.offscr_buildings.add(rect)
                        rect.rect.x -= SPEED
                    for rect in self.offscr_buildings:
                        if rect.rect.x < self.play_rect.w:
                            self.buildings.add(rect)
                            self.offscr_buildings.remove(rect)
                        rect.rect.x -= SPEED
                    self.buildings.draw(self.screen)

            group.player.rect.x += SPEED

            if pygame.sprite.spritecollideany(group.player,setup.buildings) != None:
                group.player.rect.x -= SPEED
         
        elif direction == "UP" or direction == "DOWN":
            if direction == "UP":
                SPEED *= -1
                group.player.image = group.player.back
            else:
                group.player.image = group.player.front

            if group.player.rect.y + group.player.rect.height >= self.play_rect.h:
                group.player.rect.y = self.play_rect.h - group.player.rect.height
                self.bgy -= SPEED

                if self.bgy < (0-(self.background.get_height()-self.play_rect.h)):
                    self.bgy = (0-(self.background.get_height()-self.play_rect.h))

                else:
                    self.buildings.clear(self.screen,self.background)
                    for rect in self.buildings:
                        rect.rect.y -= SPEED
                    self.buildings.draw(self.screen)
                
                    
            elif group.player.rect.y < 0:
                group.player.rect.y = 0
                self.bgy -= SPEED
                if self.bgy > 0:
                    self.bgy = 0
                else:
                    self.buildings.clear(self.screen,self.background)
                    for rect in self.buildings:
                        rect.rect.y -= SPEED
                    self.buildings.draw(self.screen)
                
                return
         
            group.player.rect.y += SPEED

            if pygame.sprite.spritecollideany(group.player,setup.buildings) != None:

                group.player.rect.y -= SPEED

        
        group.clear(self.screen,self.screen)
        group.draw(self.screen)

    def update(self):
        pygame.display.update(self.play_rect)
        self.screen.blit(self.background,(self.bgx,self.bgy))
        self.player.draw(self.screen)
        self.buildings.draw(self.screen)
        self.draw_gui()