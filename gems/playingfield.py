import datetime, logging
from random import sample
import operations
# debug | info  | warning | error | critical

logging.basicConfig(filename='gemdrop.log', level=logging.INFO)
logging.disable(logging.CRITICAL)

# the playing field is a **list of columns** that contains ints repersenting gems
def make_playing_grid(rows:int,cols:int):
    grid = [ [ 0 for i in range(rows) ] for i in range(cols) ]
    return grid

# ints 5 and above are different colors of gems, stored on the full and sub palettes
full_palette = [5, 6, 7, 8, 9, 10]
rows,cols = (6,10) # rows x columns

# 0 is the null gem, and 1-4 are the special powers.

#############################
#         Printing          #
#############################

def print_numeric_grid(grid):
    desc = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            desc += str(grid[j][i]) + " "
        desc += "\n"
    print(desc)

small_sprites = [" ", "-", "|", "~", "*", f"\033[91m@", f"\033[92m#", f"\033[93m$", f"\033[94m%", f"\033[95m&", f"\033[90m?"]

def print_colored_symbols(grid):
    desc = ""
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            desc += small_sprites[grid[j][i]] + " "
        desc += "\n"
    print(desc)

#############################
#       Main Game Loop      #
#############################

if __name__ == "__main__":
    
    logging.info(f' Started new run. {datetime.datetime.now()}')
    
    # First the color palette is shuffled and four-five colors are chosen
    palette = sample(full_palette,4)
    # First the grid loads up using the size parameter; lists are initialized
    grid = make_playing_grid(rows,cols)
    # using the gem palette, each cells is randomly filled.
    operations.fill_in_holes(grid,palette)
    print_numeric_grid(grid)
    print_colored_symbols(grid)
        # Similar to the move loop below, the grid searches and clear matches

    # Loop for remaing moves:

        # User, using sokoban/hexapawn like mvement, picks two gems to swap
            # Should probably have user select a single boarder between gems for simplicity
            # This requires a secondary grid with a strange implementation
                # (Move validation can be added later)
                # If a special gem is activated, it is marked with a negative sign
        # swap the gems

        # After every move the following happens loop the following:
            # The board is searched for a match or marked gem (top --> bottom, left --> right) 
            # when one is found, the top-left most gem is replaced with the needed int. Add score
                # all others are replaced with the null gem, 0
                # if a special gem would become a 0, activate it after current 0 search is done
            # Going column by column, all gems move downwards. Only upper cells are 0
            # All zeros in the grid are randomly filled in with gem palette
        
        # Once the board is free of matches, move counted is decremented
            # If it's zero, break.

    # At the end, count and display the score
        # May or may not search the grid and activate special gems to add more score
    
    logging.info(f' Reached the end of the code')