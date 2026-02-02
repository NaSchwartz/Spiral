import datetime, logging
from random import sample
import operations
# debug | info  | warning | error | critical

logging.basicConfig(filename='gemdrop.log', level=logging.INFO)
#logging.disable(logging.CRITICAL)

# ints 5 and above are different colors of gems, stored on the full and sub palettes
# 0 is the null gem, and 1-4 are the special powers.
full_palette = [5, 6, 7, 8, 9, 10]
cursor_position = [0,0]

#############################
#       Main Game Loop      #
#############################

if __name__ == "__main__":
    
    logging.info(f' Started new run. {datetime.datetime.now()}')
    
    # Set the number of moves and grid dimensions
    remaining_moves = 5
    rows,cols = (6,10) # rows x columns
    
    # First the color palette is shuffled and four colors are chosen.
    palette = sample(full_palette,4)

    # Next, the grid loads up using the size parameter; lists are initialized
    grid = operations.make_playing_grid(rows,cols)

    # Using the gem palette, each cell is randomly filled.
    operations.fill_in_holes(grid,palette)

    # Similar to the move loop below, the grid searches and clears matches
    #operations.remove_matches(grid, palette)

    # Loop for remaing moves:
    while remaining_moves > 0:
        # User, moving cursor, picks two gems to swap
        # If a special gem is activated, it is marked with a negative sign
        cursor_position = operations.get_user_swap(grid, rows, cols, cursor_position)
        remaining_moves -= 1

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