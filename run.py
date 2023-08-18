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


# Function to place ships on the board
def place_ship(board, ship_size):
    """
    Randomly places a ship of the given size on the game board.

    :param board: The game board to place the ship on.
    :param ship_size: The size of the ship.
    """
    while True:
        o = random.choice(['h', 'v'])
        if o == 'h':
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board[0]) - ship_size)
            if all(board[x][y+i] == '.' for i in range(ship_size)):
                for i in range(ship_size):
                    board[x][y+i] = 'S'
                break
        else:
            x = random.randint(0, len(board) - ship_size)
            y = random.randint(0, len(board[0]) - 1)
            if all(board[x+i][y] == '.' for i in range(ship_size)):
                for i in range(ship_size):
                    board[x+i][y] = 'S'
                break


# Function to play the Battleship game
def play_battleship(size, uname):
    p_board = init_board(size)
    c_board = init_board(size)
    ships = [5, 3, 3, 2, 2]
    for s in ships:
        place_ship(p_board, s)
        place_ship(c_board, s)
    # Calculate total shots based on grid size
    total_shots = 22 + (size - 5) * 6
    # Maximum shots based on grid size
    remaining_shots = total_shots
    print(f"Welcome {uname} to Battleship war!")
    print(GAME_INSTRUCTIONS)
    print_boards(p_board, c_board, size, hide_comp=True)
    # Decrease remaining shots after each player turn
    while remaining_shots > 0:
        print(f"Remaining Shots: {remaining_shots}")
        player_turn(c_board, size)
        remaining_shots -= 1

        print_boards(p_board, c_board, size, hide_comp=True)
        if is_game_over(c_board):
            print("Congrats, You win! All enemy ships are down.")
            feedback = get_feedback()
            print("Thank you for playing!")
            break

        comp_turn(p_board, size)
        print_boards(p_board, c_board, size, hide_comp=True)
        if is_game_over(p_board):
            print("Game over! The CPU sank all your ships. You lose!")
            feedback = get_feedback()
            print("Thank you for playing!")
            break

    if remaining_shots == 0:
        print("Out of shots! The battle is a draw.")
        feedback = get_feedback()
        print("Thank you for playing!")


if __name__ == "__main__":
    while True:
        size = int(input("Enter grid size (5-10): "))
        if 5 <= size <= 10:
            username = input("Enter your Name Captain: ")
            play_battleship(size, username)
            play_again = input("Play another round? (yes/no):").lower()
            if play_again == 'no':
                print("Thank you for playing!")
                break
        else:
            print("Invalid grid size. Enter a value between 5 and 10.")