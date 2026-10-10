
def draw( grid ):
    result = ""
    for l in grid:
        for c in l:
            if c == 1:
                result += "o"
            elif c == 0:
                result += "x"
            else:
                result += "t"
        result += "\n"
        
    return result


def countNeighbors( grid ):
    # iterate over grid list to find living cells : if a cell is alive then it adds a neighbor to evry cells ina grid of 3x3 cells around
    #
    # took me 2h to know that temp = grid[:] followed by the program changed grid[...][...] while changing temp[...][...]
    # now, temp is totaly independent :
    temp = [ [0 for columns in lines] for lines in grid ] # edit a temp grid to keep data of current grid for process
    lines = len(grid)
    columns = len(grid[0])
    y = 0 # y => lines
    x = 0 # x => columns


    for l in grid:      # lines in grid => y
        for c in l:     # columns in lines => x
            if c == 1:  # add 1 to neighbors of living cells
                        # system to increase neighboring cells depending on coords
                left = False
                right = False
                up = False
                down = False

                if x > 0 and x < columns-1: # if cell is not in grid borders' columns
                    left = True
                    right = True
                else:                       # if cell is in grid borders' columns
                    if x == 0:
                        right = True
                    else:
                        left = True
                
                if y > 0 and y < lines-1:  # if cell is not in grid borders' lines
                    up = True
                    down = True
                else:                      # if cell is in grid borders' lines
                    if y == 0:
                        down = True
                    else:
                        up = True


                if right:                   # if cell has neighbors on her right
                    temp[y][x+1] += 1       # add 1 to right cell
                    if up:                      # if cell has neighbors upward
                        temp[y-1][x+1] += 1     # add 1 to upper right cell
                    if down:                    # if cell has neighbors downward
                        temp[y+1][x+1] += 1     # add 1 to lower right cell
                
                if left:                    # if cell has neighbors on her left
                    temp[y][x-1] += 1       # add 1 to left cell
                    if up:                      # if cell has neighbors upward
                        temp[y-1][x-1] += 1     # add 1 to upper left cell
                    if down:                    # if cell has neighbors downward
                        temp[y+1][x-1] += 1     # add 1 to lower left cell

                if up:                      # if cell has neighbors upward
                    temp[y-1][x] += 1       # add 1 to upper cell
                if down:                    # if cell has neighbors downward
                    temp[y+1][x] += 1       # add 1 to lower cell
                    

            x += 1 # increment to next column

        x = 0      # reset to first column
        y += 1     # increment to next line
            
    return temp


def nextGrid( grid, color_grid ): 
    # uses countNeighbors function to create a list with number of neighbors of each grid
    # then verify rules for each grid : living if 3 neighbors, keeping state if 2, dead for anything else
    neighbors_grid = countNeighbors(grid)
    new_grid = [] # edit a temp grid to keep data of current grid for process
    old_color_grid = color_grid
    color_grid = []
    y = 0         # line
    x = 0         # column

    for l in neighbors_grid:
        new_grid.append([])
        color_grid.append([])


        for cell in l:

            if cell == 3:   # set cell to living state if it has 3 neighbors
                new_grid[y].append(1)
                if grid[y][x] == 1:
                    color_grid[y].append(1) # blue
                else:
                    color_grid[y].append(2) # green


            elif cell == 2: # keep cell to current state if it has 2 neighbors
                if grid[y][x] == 1: 
                    new_grid[y].append(1)
                    color_grid[y].append(1) # blue

                else:
                    new_grid[y].append(0)
                    color_grid[y].append(0) # no color


            else:           # set cell to dead state for any other cases
                new_grid[y].append(0)
                if old_color_grid[y][x] == 2:
                    color_grid[y].append(4) # yellow
                else:
                    if grid[y][x] == 1:
                        color_grid[y].append(3) # red
                    else:
                        color_grid[y].append(0) # no color


            x += 1 # increment to next column

        x = 0      # reset to first column
        y += 1     # increment to next line
    
    return new_grid, color_grid

