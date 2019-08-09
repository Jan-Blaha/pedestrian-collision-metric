# from path_search_2dalg import find_path
from path_search_3dalg import find_path


# choose the best source and goal from given lists, on grid
def choose_goal(grid, sources, goals):
    minprize = None  # minimal prize
    optpath = None  # path with minimal prize

    for i in range(len(sources)):
        for j in range(len(goals)):
            prize, path = find_path(grid, sources[i], goals[j])
            if minprize is not None:
                if prize < minprize:
                    minprize = prize
                    optpath = path
            else:
                minprize = prize
                optpath = path

    return minprize, optpath


# from list of grids find the best
def choose_time(grids, source, goal):
    minprize = None  # minimal prize
    optgrid = None  # number of the best grid
    optpath = None

    for i in range(len(grids)):
        prize, path = find_path(grids[i], source, goal)
        if minprize is not None:
            if prize < minprize:
                minprize = prize
                optgrid = i + 1
                optpath = path
        else:
            minprize = prize
            optgrid = i + 1
            optpath = path

    return minprize, optgrid, optpath


def choose_time_goal(grids, sources, goals):  # returns minimal prize
    minprize = None  # minimal prize
    optgrid = None  # number of the best grid
    bestpath = None  # path with minimal prize

    for i in range(len(grids)):
        prize, path = choose_goal(grids[i], sources, goals)
        if minprize is not None:
            if prize < minprize:
                minprize = prize
                optgrid = i + 1
                bestpath = path
        else:
            minprize = prize
            optgrid = i + 1
            bestpath = path

    return minprize, optgrid, bestpath
