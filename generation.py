import setup, pygame
from random import randint
from mapmatrix import map_matrix

def item_generation(map, map_width, map_height):
    """
    Generates an item to a random point on the map using randint periodically.
    """
    i = randint(0, map_width)
    j = randint(0, map_height)

    if map_matrix[i][j] == 0:
        pass
        #setup.loadItem(

