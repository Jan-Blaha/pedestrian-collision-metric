import path_search_3dalg
import path_search_addon


# find optimal path in grid
def find_opt_path(array):  # wants parameters like (grid, source, goal)
    return path_search_3dalg.find_path(array[0][0], array[1][0], array[2][0])


# choose start and final positions and find the best path
def choose_positions(array):  # wants parameters like (grid, sources, goals)
    return path_search_addon.choose_goal(array[0][0], array[1], array[2])


# choose the best grid and find the best path init
def choose_grid(array): # wants parameters like (grids, source, goal)
    return path_search_addon.choose_time(array[0], array[1][0], array[2][0])


# choose start and final positions and the best grid and find optimal path
def choose_grid_positions(array): # wants parameters like (grids, sources, goals)
    return path_search_addon.choose_time_goal(array[0], array[1], array[2])