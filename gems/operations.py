from random import randint, choice
import logging, math
import readchar

logging.basicConfig(filename='gemdrop.log', level=logging.INFO)

##############################
#          Printing          # COMPLETE (unless we want to make a larger and more detailed grid)
##############################

def print_numeric_grid(grid):
    desc = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            desc += str(grid[j][i]) + " "
        desc += "\n"
    print(desc)

small_sprites = [" ", "-", "|", "~", "*", f"\033[91m@", f"\033[92m#", f"\033[93m$",f"\033[94m%", f"\033[95m&", f"\033[90m?", f"\033[97m"]
no_color_small_sprites = [" ", "-", "|", "~", "*", "@", "#", "$", "%", "&", "?", "+"]

def print_colored_symbols(grid):
    desc = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            desc += small_sprites[grid[j][i]] + " "
        desc += "\n"
    print(desc)

def print_symbols_with_cursor(grid, cursor_position, select1, select2):
    desc = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if [i, j]==cursor_position:
                desc += small_sprites[11] + "+" + " "
            elif [i, j] == select1:
                desc += small_sprites[11] + no_color_small_sprites[grid[j][i]] + " "
            elif [i, j] == select2: 
                desc += small_sprites[11] + no_color_small_sprites[grid[j][i]] + " "
            else:
                desc += small_sprites[grid[j][i]] + " "
        desc += "\n"
    print(desc)

##############################
#          Grid Ops.         #
##############################

def make_playing_grid(rows:int,cols:int):
    grid = [ [ 0 for i in range(rows) ] for i in range(cols) ]
    return grid

marked_stack = []

def activate_marked_gem(position:(int,int)):
    # A stack is needed to keep track of gems to hit, this function will get much more complicated
    pass

def percolate_zeros(column):
    sort_column = [0]*len(column)
    index = 0
    j = len(column)-1
    
    for i in range(j,-1,-1):
        if column[i] == 0:
            continue
        
        sort_column[j] = column[i]
        j -= 1

    return sort_column

def move_all_gems_downwards(grid):
    for column in grid:
        column = percolate_zeros(column) 

        if column[0] < 0:
            raise Exception("activated gem moved upwards!")

def fill_in_holes(grid, palette):
    for column in grid:
        for i in range(len(column)):
            if column[i] == 0:
                column[i] = choice(palette)

##############################
#       Match Searching      #
##############################

# Don't really know hoe to structure this part...

def searchgrid():
    # For anything: matches / marks
    pass

def remove_matches(grid):
    # will be called once the grid is first made, but before user's first move
    pass


##############################
#         User Inputs        # COMPLETE
##############################

def get_user_swap(grid, grid_rows : int, grid_cols : int, current_position = [0,0]) -> (int,int):
    logging.info("Entered get_user_swap")

    selected_tile1 = [None,None]
    while True:
        selected_tile2 = [None,None]
        while True:

            # print grid
            print_symbols_with_cursor(grid, current_position, selected_tile1, selected_tile2)

            match (readchar.readkey()):
                case "w":
                    current_position[0] = (current_position[0] - 1) % grid_rows
                case "s":
                    current_position[0] = (current_position[0] + 1) % grid_rows
                case "a":
                    current_position[1] = (current_position[1] - 1) % grid_cols
                case "d":
                    current_position[1] = (current_position[1] + 1) % grid_cols
                case " ":
                    if selected_tile1 == [None,None]:
                        # if 1 isn't selected, select it
                        selected_tile1 = current_position.copy()
                    elif selected_tile1 == current_position:
                        # if 1 needs to be toggled, toggle it
                        selected_tile1 = [None,None]
                    elif selected_tile2 == [None,None]:
                        # if 2 isn't selected, select it
                        selected_tile2 = current_position.copy()
                        # both tiles selected, break, check if valid swap
                        break
                    elif selected_tile2 == current_position:
                        # if 2 needs to be toggled, toggle it
                        selected_tile2 = [None,None]
                    else:
                        raise Exception("It should not be possible to get this error!")
                case _:
                    continue
            
        if valid_swap(selected_tile1, selected_tile2, grid):
            # swap is done, return current cursor position for better flow
            return current_position
        # else, not valid, restart just tile 2

def valid_swap(position1 : (int,int), position2 : (int,int), grid) -> bool:
    # Should be impossible for pos1 == pos2 to happen
    grid_adjacent = abs(position1[0]-position2[0]) + abs(position1[1]-position2[1]) 
    if grid_adjacent == 1:
        do_gem_swap(position1, position2, grid)
        return True
    return False

def do_gem_swap(position1 : (int,int), position2 : (int,int), grid) -> bool:
    # First, swap both gems
    temp = grid[position1[1]][position1[0]]
    grid[position1[1]][position1[0]] = grid[position2[1]][position2[0]]
    grid[position2[1]][position2[0]] = temp

    # If either gems are special gems, activate them
    if grid[position1[1]][position1[0]] <= 4:
        grid[position1[1]][position1[0]] *= -1
    if grid[position2[1]][position2[0]] <= 4:
        grid[position2[1]][position2[0]] *= -1
