"""
Legend:
1. "." = Water or empty space.
2. "s" = Ships, Ship positions.
3. "#" = Water shot with bullets, a miss it hit no ship.
4. "x" = Ship Hit!

Battleship:
A. grid = 10x10Custom grids between min 5 to max 10.
B. 5 ships of variable length were randomly placed.
C. Every hit or miss shot will show up in the grid.
D. If all ships are unearthed before using up all bullets,
You Win else, You lose.
E. You can choose a row and column such as A1, B1 to indicate where to shoot.
"""

import random

# Constants and globals
"""EMPTY = ''' . '''
SHIP = ''' S '''
HIT = ''' X  '''
MISS = ''' # '''
GRID_SIZE = ''' Between 5 to 10 '''
SHIPS = [5, 3, 3, 2, 2]  # Variation sizes of ships
NUM_SHIPS = 5"""

GAME_INSTRUCTIONS = """
INSTRUCTIONS!!!
1. Enter your grid size.
2. Enter Your Name.
3. Enter your coordinates on the map to sink the enemy's fleet e.g. A0, B1.
4. Player will have limited shots as per grid size.
Now you're ready for the Naval war Captain. GOOD LUCK!
"""


# Function to initialize the game boards
def init_board(size):
    return [['.' for _ in range(size)] for _ in range(size)]

# Function to print the game boards
def print_boards(player, computer, size, hide_comp=True):
    """
    Prints the player and computer game boards side by side.

    :param player: The player's game board.
    :param computer: The computer's game board.
    :param size: The size of the game board.
    :param hide_comp: If True, hides the computer's ship positions.
    """
    col_labels = " ".join(chr(65 + i) for i in range(size))
    print(f"{username} Board:      CPU Board:")
    print("   " + col_labels + "   " + "   " + col_labels)
    for i in range(size):
        comp_row = [
            '.' if c == 'S' else c for c in computer[i]
        ] if hide_comp else computer[i]
        row_str = f"{i}  {' '.join(player[i])}   {i}  {' '.join(comp_row)}"
        print(row_str)
