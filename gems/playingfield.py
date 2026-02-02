import operations

size = (6,10) # rows x columns

# the playing field is a **list of columns** that contains ints repersenting gems
# ints 5 and above are different colors of gems
# 0 is the null gem, and 1-4 are the special powers.

# # # Main game loop # # #


# First the grid loads up using the size parameter; lists are initialized
# using the gem palette, each cells is randomly filled.
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