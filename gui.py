import pygame,animation
from pygame import sprite
import setup, random
from collections import namedtuple
from textwrap import drawText
from auto_eat import auto_eat
from item import *


# GUI size things
RESOLUTION_RECT = pygame.Rect(0,0, 600,400)
BUTTON_HEIGHT = 40
BUTTON_WIDTH = 100
HOVER_HEIGHT = 100
HOVER_WIDTH = 175
GUI_WIDTH = 200
MAP_WIDTH = 400
BAR_WIDTH = 100
INV_HEIGHT = 220
INV_WIDTH = 190
PAD = 5
TILE_SIZE = 20

# Set fonts
pygame.font.init()
SMALLER_FONT_SIZE = 10
SMALL_FONT_SIZE = 14
FONT_SIZE = 16
BIG_FONT_SIZE = 18
SMALLER_FONT = pygame.font.SysFont("Arial", SMALLER_FONT_SIZE)
SMALL_FONT = pygame.font.SysFont("Arial", SMALL_FONT_SIZE)
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
BIG_FONT.set_bold(True)
FONT_COLOUR = (0, 0, 0)

# Colour stuff
GUI_COLOUR = (150, 150, 150)
SEL_COLOUR = (0,255,255)
OUTLINE_COLOUR = (255, 255, 255)
BUTTON_HIGHLIGHT_COLOUR = (255, 255, 255)
BUTTON_DISABLED_COLOUR = (64, 64, 64)
RED_BAR = (255,0,0)
GREEN_BAR = (0,255,0)

DROP_RATE = 0.7
STAMINA_LOSS = 10
ENCUMBERED_VAL = 70
HUNGER_VAL = 70


# A container class which stores button information.
# slot_height and slot_width represents the number of BUTTON_HEIGHT and BUTTON WIDTH of the button relative to the bottom and right edge of gui.
Button = namedtuple('Button', ['slot_x', 'slot_y', 'rect','text', 'onClick', 'condition'])

class GUI():
    """ 
    Graphic User Interface class
    Handles GUI drawing, gui button behavior, and some animations.
    """
    
    num_instances = 0
    def __init__(self):
        
        if GUI.num_instances != 0:
            raise Exception("GUI can only have one instance of a simulation")
        num_instance = 1
        
        self.screen = setup.screen
        self.screen_rect = RESOLUTION_RECT
                                    
        self.background = setup.background
        self.bgx = setup.bgx
        self.bgy = setup.bgy
        self.player = setup.player
        self.buildings = setup.buildings
        self.items = setup.items
        
        #timers
        self.timer = 0
        self.auto_timer = 0
        self.can_auto = True
        self.last_item = None
        self.has_stamina = True
    
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
        temp_rect = pygame.Rect(0,0,1,1)
        self.buttons = [
            Button(1, 1, temp_rect, "USE", self.use_pressed, self.item_selected),
            Button(0, 1, temp_rect, "DISCARD", self.discard_pressed, self.item_selected),
            Button(0, 0, temp_rect, "SEARCH", self.search_pressed, None),
            Button(1, 0, temp_rect, "AUTO-EAT", self.auto_pressed, self.can_click_auto)]
    
        #Currently Selected Item in Inventory
        self.sel_item = None
    
    def draw_gui(self):
        """
        Draws the interface on the right side of the screen.
        Some 'magic' numbers are hardcoded because of the specific layout.
        """
        if not self.background: return
    
        line_num = 0

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
        hunger_rect.x, hunger_rect.y = RESOLUTION_RECT.w - (self.gui_rect.w)/2 - PAD, FONT_SIZE*line_num + 2*PAD
        hunger_rect.w = self.player.hunger
        bar_colour  = RED_BAR if self.player.hunger >= HUNGER_VAL else GREEN_BAR
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
        if self.player.stamina >= 0:
            stamina_rect.w = self.player.stamina
        else:
            stamina_rect.w = 0
        bar_colour = RED_BAR if self.player.stamina <= 30 else GREEN_BAR
        pygame.draw.rect(self.screen,bar_colour, stamina_rect)
        # encumbered state
        if self.player.encumbrance > ENCUMBERED_VAL:
            player_encumbered = SMALLER_FONT.render("ENCUMBERED", True, RED_BAR)
            self.screen.blit(player_encumbered,
                        (stamina_rect.x+ 3*PAD,
                          stamina_rect.y + 2*PAD))
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
        Draws the list of items (inventory) into the gui. Also handles cursor
        highlighting items and item selection.
        If there are multiples of an item, keep the item selected.
        """
        inventory_rect = self.gui_rect.copy()
        inventory_rect.x += PAD
        inventory_rect.y += 85
        inventory_rect.w = INV_WIDTH
        inventory_rect.h = INV_HEIGHT
        
        count_rect = pygame.Rect(self.screen_rect.w - 5*PAD, 0, 4*PAD, INV_HEIGHT/10)
        
        # item number display parameters
        inv_line = 0
        count_dict = {}
        # dictionary of display coordinate tuples
        item_whichline = {}

        for item in self.player.inventory:
            
            #assigning the rect of item displayed
            #if an instance of the item does not exist in displayed inventory
            if not item.name in count_dict:
                item.list_rect = inventory_rect.copy()
                item.list_rect.x += 1
                item.list_rect.w -= 2
                item.list_rect.h = INV_HEIGHT/10
                item.list_rect.y += inv_line * item.list_rect.h
                # keep track of the item location in the displayedlist
                item_whichline[item.name] = (item.list_rect.x,item.list_rect.y)
                count_dict[item.name] = 1
                inv_line +=1
    
            
            else:
                #get the item location of the same item in the displayed list
                item.list_rect.x, item.list_rect.y = item_whichline[item.name][0], item_whichline[item.name][1]
                item.list_rect.h = INV_HEIGHT/10
                item.list_rect.w = inventory_rect.w - 2
                
                count_dict[item.name] += 1
            
            # clear the rect of text
            pygame.draw.rect(self.screen, GUI_COLOUR, item.list_rect)
            
            # create the window for hovering over items
            mouse_pos = pygame.mouse.get_pos()
            if item.list_rect.collidepoint(mouse_pos):
                self.draw_hover_rect(item)
                pygame.draw.rect(self.screen, OUTLINE_COLOUR, item.list_rect)
            
            
            
            # draw the name of the item on top of everything else
            item_name = SMALL_FONT.render(item.name,
                                        True,
                                        FONT_COLOUR)

            self.screen.blit(item_name,
                            (inventory_rect.x + PAD, item.list_rect.y+PAD))
            #update the item count inventory
            item_count = SMALL_FONT.render(str(count_dict[item.name]),
                                                True,
                                                FONT_COLOUR)
            self.screen.blit(item_count,
                            (count_rect.x, item.list_rect.y+PAD))
            
        # draw the inventory box outline
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, inventory_rect, 1)

        # draw the outline around the selected item, otherwise clear it
        if self.sel_item:
            pygame.draw.rect(self.screen, SEL_COLOUR, self.sel_item.list_rect,1)

        #draw message dialogue for the last item picked up
        if self.last_item:
            self.draw_message_rect(SEL_COLOUR, self.last_item.name, itmfound = True)
        #Player has stamina?
        if not self.has_stamina:
            self.draw_message_rect(RED_BAR,"Not enough stamina.")


    def draw_hover_rect(self, item):
        """
        Draw the popup menu that appears when an item is hovered over.
        Displays item name and description when hovering over an item in the inventory.
        """
        hover_rect = pygame.Rect(self.gui_rect.x - HOVER_WIDTH, 0,HOVER_WIDTH, HOVER_HEIGHT)
        hover_out_rect = hover_rect.copy()
        hover_out_rect.w -= 1
        hover_out_rect.h -= 1
        
        item_name = item.name
        item_desc = item.description

        pygame.draw.rect(self.screen, GUI_COLOUR, hover_rect)
        pygame.draw.rect(self.screen, OUTLINE_COLOUR, hover_out_rect, 2)
        
        text_rect = hover_rect.copy()
        text_rect.x += PAD
        text_rect.y += PAD
        
        # drawText utilizes text wrapping
        # this function is imported from textwrap.py
        drawText(self.screen, item_name, FONT_COLOUR, text_rect, SMALL_FONT)
        text_rect.y += PAD + FONT_SIZE
        drawText(self.screen, item_desc, FONT_COLOUR, text_rect, SMALL_FONT)
    
    def draw_message_rect(self, txtcolour, msg, itmfound = False):
        if (self.timer <1): #6 second interval
            msg_rect = pygame.Rect(self.gui_rect.x - HOVER_WIDTH, self.screen_rect.h-HOVER_HEIGHT, HOVER_WIDTH, HOVER_HEIGHT/2)
            msg_out_rect = msg_rect.copy()
            msg_out_rect.w -= 1
            msg_out_rect.h -= 1
        
            pygame.draw.rect(self.screen, GUI_COLOUR, msg_rect)
            pygame.draw.rect(self.screen, OUTLINE_COLOUR, msg_out_rect, 2)
            
            text_rect = msg_out_rect.copy()
            text_rect.x += PAD
            text_rect.y += PAD
    
            if itmfound:
                drawText(self.screen, "Found item:", FONT_COLOUR, text_rect, SMALL_FONT)
                text_rect.y += PAD + FONT_SIZE
            drawText(self.screen, msg, txtcolour, text_rect, SMALL_FONT)
    
        else:
            self.last_item = None
            self.timer = 0
            self.has_stamina = True
    
    def draw_gui_button(self, button):
        """
        Renders a button to the bar.
        If the mouse is hovering over the button it is rendered in white,
        else grey.
        The button is disabled if conditions to click it are not met.
        """
        but_x = self.screen_rect.w - (self.gui_rect.w/2)*(button.slot_x+1) + PAD
        but_y = self.screen_rect.h - (self.gui_rect.h/9)*(button.slot_y+1) 
        but_rect = pygame.Rect(but_x,
                                but_y,
                                BUTTON_WIDTH,
                                BUTTON_HEIGHT)
        
        # The outline needs a slightly smaller rectangle
        but_out_rect = but_rect
        but_out_rect.width -= 2*PAD

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

        # Special case: search button bolds when on searchable area
        if button.text == "SEARCH":
            if pygame.sprite.spritecollideany(self.player.player,
                                                setup.longgrass) or\
                pygame.sprite.spritecollideany(self.player.player,
                                                setup.items) or\
                self.search_log_possible(self.player.player,self.player.get_dir()):
                but_text = FONT.set_bold(True)
        
        # Draw the text
        but_text = FONT.render(button.text, True, FONT_COLOUR)


        self.screen.blit(
            but_text,
            (but_rect.centerx - (but_text.get_width()/2),
            but_rect.y + (BUTTON_HEIGHT/2) - but_text.get_height()/2))
        but_text = FONT.set_bold(False)
                
    
    def use_pressed(self):
        """
        Use button is clicked while an inventory item is selected.
        """
        if self.sel_item == None:
            print("no item selected")
            return
        #if the item is usable, consume it and remove it from inventory
        self.sel_item.consume_item(self.player)
        for i in self.player.inventory:
            # if there are still items of that type in the inventory, keep it selected
            if i.name == self.sel_item.name:
                self.sel_item = i
                return
        self.sel_item = None

    def discard_pressed(self):
        """
        Discard button is clicked while an inventory item is selected.
        """
        if self.sel_item == None:
            return
        self.sel_item.discard(self.player)
        # if there are still items of that type in the inventory, keep it selected
        for i in self.player.inventory:
            if i.name == self.sel_item.name:
                self.sel_item = i
                return
        self.sel_item = None

    def search_pressed(self):
        """
        Search for usable items on the current and adjacent positions of the player
        """
        #check collision between player and grass
        in_grass = pygame.sprite.spritecollideany(self.player.player, setup.longgrass)

        #check collision between player and any item on the ground
        eligible_item = pygame.sprite.spritecollideany(self.player.player,self.items)
        if eligible_item and eligible_item.name != "Fire":
            eligible_item.pick_up(self.player)
            self.items.remove(eligible_item)
        

        elif in_grass:
            #reduce stamina
            if self.player.stamina < 20:
                print("no stamina")
                self.has_stamina = False
                return
            else:
                self.player.stamina -= 20
            i_rand = random.randint(1,9)
            rand_p = random.random()
            if rand_p > (1-DROP_RATE):
                eligible_item = setup.generateItem(i_rand)
                if eligible_item:
                    eligible_item.pick_up(self.player)
                    eligible_item.set_inventory()
    
        #Check if a log is in front
        elif self.search_log_possible(self.player.player, self.player.get_dir()):
            #reduce stamina
            if self.player.stamina < 20:
                self.has_stamina = False
                return
            else:
                self.player.stamina -= 20
            rand_p = random.random()
            if rand_p > (1-DROP_RATE):
                eligible_item = firewood.Firewood()
                eligible_item.pick_up(self.player)
                eligible_item.set_inventory()
        
        if eligible_item: #is found
            self.last_item = eligible_item
            
            self.timer = 0


    def search_log_possible(self, player, dir):

        search_rect = pygame.Rect(player.rect.x,player.rect.y,TILE_SIZE,TILE_SIZE)
        if dir == "UP":
            search_rect.y -= TILE_SIZE
        elif dir == "RIGHT":
            search_rect.x += TILE_SIZE
        elif dir == "LEFT":
            search_rect.x -= TILE_SIZE
        elif dir == "DOWN":
            search_rect.y += TILE_SIZE
        
        for b in setup.logs:
            if search_rect.colliderect(b.rect):
                return b

    def auto_pressed(self):
        """
        Calls auto-use function based on which stat is selected.
        Optimally consumes the items that restores the most hunger
        and out of the items that relieves encumbrance.
        Relieves half of encumbrance.
        If encumbered, auto eat should eat until player is no longer encumbered, then eat until half encumbered
        
        """
   
        print("player hunger: {}".format(self.player.hunger))
        print("player encbrn: {}".format(self.player.encumbrance))
        consum_list = self.player.inventory.copy()
        
        remain = int(self.player.encumbrance/2)
        if self.player.encumbrance > ENCUMBERED_VAL:
            remain = self.player.encumbrance
        print("target remain ",remain)
        # lambda is currently mapping the amount of hunger an item restores
        to_consume = auto_eat(remain,consum_list,lambda x: -1*x.hung_value)

        hung = 0
        enc = 0
        if to_consume:
            self.can_auto = False
            for i in to_consume:
                i.consume_item(self.player)
                hung -= i.hung_value
                enc += i.size
        print("Hung restored: {} player hunger: {} encb: {}".format(hung, self.player.hunger, enc))
    
    
    def item_selected(self):
        """
        An item in the inventory is clicked/selected. Returns true or false.
        """
        if self.sel_item: return True
        else: return False
    
    def can_click_auto(self):
        if self.can_auto: return True
        else: return False
    
    def on_click(self,e):
        """
        Handles clicking events.
        """
        if (e.type == pygame.MOUSEBUTTONUP
            and e.button ==1
            and pygame.mouse.get_focused()):
            
            # if the inside of the gui was clicked
            if self.gui_rect.collidepoint(e.pos):
                itm = self.get_item_at_point(e.pos)
                if self.sel_item == None:
                    self.sel_item = itm
            
                # if the click position is not on an item, check for button
                if not itm:
                    object = self.get_button_at_point(e.pos)
                    if object: object.onClick()

    def get_item_at_point(self,pos):
        """
        Returns the item if the inventory position is within its rect
        """
        for i in self.player.inventory:
            if i.list_rect.collidepoint(pos):
                self.sel_item = i
                return i
    
    def get_button_at_point(self,pos):
        """
        Detects if a button or item is clicked at a given mouse position.
        If a button is detected
        """

        for button in self.buttons:
            # If the button is enabled and clickable, call the click function
            if not button.condition or button.condition():
            
                # Temporarily construct the button rect
                but_x = self.screen_rect.w - (self.gui_rect.w/2)*(button.slot_x+1) + PAD
                but_y = self.screen_rect.h - (self.gui_rect.h/9)*(button.slot_y+1)
                but_rect = pygame.Rect(but_x,
                                but_y,
                                BUTTON_WIDTH,
                                BUTTON_HEIGHT)
                # if the mouse position is on the button
                if but_rect.collidepoint(pos):
                    print("{} was clicked".format(button.text))
                    return button
    
    def killPlayer(self):
        DELAY = 200

        deadgus = pygame.image.load("images/deadgus.png").convert_alpha()
        p = setup.player.player
        for i in range(0,4):
            animation.handleAnimation(p,p.dir)
            self.update()
            pygame.time.delay(DELAY)
            p.dir += 1
            if p.dir > 3:
                p.dir = 0 
        while p.dir != 1:
            p.dir += 1
            if p.dir > 3:
                p.dir = 0 
            animation.handleAnimation(p,p.dir)
            self.update()
            pygame.time.delay(DELAY)
        p.image = deadgus
        self.update()
        pygame.time.delay(DELAY)
        
    def update_timer(self):
        #increments every 6 seconds as per pygame clock in main
        self.timer +=1
        self.auto_timer += 1

    def update(self):
        """
        Update the drawing of everything display related.
        """
        self.screen.blit(self.background,(self.bgx,self.bgy))
        is_fire = False
        for spr in setup.items:
            if spr.name == "Fire":
                animation.handleAnimation(spr,0)
                is_fire = True

    
        # prevent player from constantly clicking auto
        if self.auto_timer > 4:
            self.can_auto = True
            self.auto_timer = 0
        for spr in setup.npcs:
            animation.handleAnimation(spr,spr.dir)
        setup.items.draw(self.screen)
        
        setup.logs.draw(self.screen)
        setup.npcs.draw(self.screen)
        self.player.draw(self.screen)
        self.buildings.draw(self.screen)
        setup.longgrass.draw(self.screen)
        setup.trees.draw(self.screen)


        self.draw_gui()
        pygame.display.flip()