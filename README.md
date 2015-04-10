## Survive! A CMPUT275 Project
A small game created by Brad Sidoruk and Christina Ho for CMPUT 275 Winter 2015 at the University of Alberta 
Python3 and pygame are required to run the game. Survive the elements as Gus in this mini-survival sandbox game by staving off hunger and wolves.

# Instructions
To play the game, in the main directory with main.py, run the game with the command
> python3 main.py

Controls:
>   WASD    - Movement
>   Cursor is used to interact with the gui. Hotkeys are available as follows:
>   SPACE   - Hold to sprint
>   ESC     - Quit game
>   ENTER   - Search the area around you
>   RSHIFT  - Auto-eat
    

How long can you survive? There are various places to look for supplies. The search button indicates searchable spots around the woods. The more items you carry, the more tired you'll be when moving around.
Your hunger increases as you wander and explore. The more tired you are, the hungrier you get. 
The woods are home to some rabbits and wolves. Without any gear, Gus is not able to hunt for rabbits or defend himself from wolves, so pick your paths wisely.
Fire can be created if there is sufficient firewood and flint.

# CMPUT275 Stuff
One of the primary requirements of this project was to create algorithmically challenging problems. For our project, we included an "auto-eat" function that effectively maximizes the amount of hunger you can relieve based on your inventory size. The function produces a subset of items from the player's inventory that has the higher "hunger" value, and is the "size" or weight of half of the weight of the total inventory. Essentially, the auto-eat function relieves half of the inventory weight and provides the best amount of consumable value out of all possible subsets.

Pygame module were used extensively in this project as well as animations. Custom item and npc modules were created. All sprites and images were custom created. Code that was referenced are cited in the appropriate files.
