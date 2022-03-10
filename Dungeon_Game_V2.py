import logging
import random

logging.basicConfig(filename="Dungeon_Game_Log", level=logging.DEBUG)

#   Draw grid
#   Pick random location for player
#   Pick random location for exit door
#   Pick random location for the monster
#   Draw the player in the grid
#   Take input for movement
#   Move player, unless invalid move (past edges of grid)
#   Check for win/loss
#   Clear screen and redraw grid


def create_cells():
    line = 0
    cell = []
    while line < height:
        row = 0
        while row < length:
            cell.append((row, line))
            row += 1
        line += 1
    return cell


"""
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
"""


def clear2():
    print("\n" * 2)


def get_locations():        # .choice(list) can give the same position so we use .sample(list,Number of different cases)
    return random.sample(create_cells(), 3)


def move_player(player, move):

    # Get the player's location
    x, y = player

    # If move == LEFT,  x-1
    if move == "LEFT":
        x -= 1

    # If move == RIGHT, x+1
    if move == "RIGHT":
        x += 1

    # If move == UP,  y-1
    if move == "UP":
        y -= 1

    # If move == DOWN, y+1
    if move == "DOWN":
        y += 1

    return x, y


#   return the available moves depends on the player's location
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    x, y = player

    # if player's x == 0,   they cant move left
    if x == 0:
        moves.remove("LEFT")

    # if player's x == 4,   they cant move right
    if x == length:
        moves.remove("RIGHT")

    # if player's y == 0,   they cant move up
    if y == 0:
        moves.remove("UP")

    # if player's y == 4,   they cant move down
    if y == height:
        moves.remove("DOWN")

    return moves


def draw_map(player):   # ▲ ●
    print(" _" * length)
    tile = "|{}"

    for cell in create_cells():
        x, y = cell

        if x < length-1:
            line_end = ""

            if cell == player:
                output = tile.format("●")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"

            if cell == player:
                output = tile.format("●|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    clear2()
    # we assign the location outside the loop we it wont change a each iteration
    monster, door, player = get_locations()
    # save the positions to help on debug
    logging.info("Monster: {}, Door: {}, Player: {}".format(monster, door, player))

    playing = True

    while playing:
        draw_map(player)
        print()
        valid_moves = get_moves(player)

        print("You're currently in room {}".format((player[0]+1, player[1]+1)))        # fill with player position
        print("You can move {}".format(", ".join(valid_moves)))        # fill with available move
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move == "QUIT":
            print("\n ** See you next time! ** \n")
            break

        # Good move? change the player position
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** Oh no! The monster got you! better luck next time **\n")
                playing = False

            if player == door:
                print("\n** You escaped! Congratulations! **\n")
                playing = False

        # Bad move? don't change anything!
        elif move in ["LEFT", "RIGHT", "UP", "DOWN"]:
            print("\n ** Walls are hard! Don't run into them **\n")

        else:
            input("\n ** This is not a valide Direction **\n")

    else:
        if input("Play again? [Y/n]   ".lower()) == "y":
            game_loop()
        # On the door? they win!
        # On the monster? they lose!
        # Otherwise, loop back around!


clear2()
print("Welcome to the dungeon! \n")

try:
    a = int(input("Please enter the Length on the map   "))
    b = int(input("Please enter the Height on the map   "))
except ValueError or NameError:
    print("\n ** The input must be an Int number! **")
    print("\n ** The dimensions should be greater than 2 **")
    exit()

else:
    if a < 2 or b < 2:
        print("\n ** The dimensions should be greater than 2 **")
        exit()
    else:
        length = a
        height = b
clear2()
game_loop()
