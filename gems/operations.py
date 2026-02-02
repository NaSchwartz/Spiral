from random import randint, choice
import logging
#from enum import Enum

logging.basicConfig(filename='gemdrop.log', level=logging.INFO)

##############################
#          Grid Ops.         #
##############################

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

##############################
#         User Inputs        #
##############################

def create_user_grid():
    '''
    This is what the grid looks like:
    
    + - + - + - + - +                                                
    |   |   |   |   |            |   |   |                0   0   0    
    + - + - + - + - +          -   -   -   -            0   0   0   0       0 0 0 0 0 0 0 
    |   |   |   |   |  --->      |   |   |      --->      0   0   0    ---> 0 0 0 0 0 0 0 
    + - + - + - + - +          -   -   -   -            0   0   0   0       N 0 N 0 N 0 N 
    |   |   |   |   |            |   |   |                0   0   0    
    + - + - + - + - +                                   N   N   N   N
                                                                       
    
    ie 3x4 grid of cells becomes 3x7
    nxm ---> nx(2m-1)
    This grid is a **list of columns**
    '''
    pass

# a swap is very easy to hard code, but translating it this way is harder

def translate_execute_swap(gem_grid, user_grid, user_swap_position:(int,int)):
    # If the swap contains a special gem (0<int<5) mark it with a negative sign
    pass

def valid_swap(grid_to_test) -> bool:
    # do this at the end, near final draft

    # unsure the most efficient way to do this
    # Currently: search "new" grid for a match/marked gem, return bool
    pass


##############################
#        Miscellaneous       #
##############################

# class for color changes(?)