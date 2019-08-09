# works with 3d grid, that means 2d grid where each node has 4 layers which represents directions
# reprezentace gridu (radek, sloupec, smer)

# directions - positions in array [LEFT, RIGHT, UPPER, BOTTOM]
LEFT = 0
RIGHT = 1
UPPER = 2
BOTTOM = 3


def euklid(a, b):  # euklid metrics
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) ** 0.5


def manhattan(a, b):  # manhattan metrics
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Node:
    visited = None
    grid = None
    age = 0

    def __init__(self, x, y, z):  # x = row, y = col, z = direction
        self.coord = (x, y, z)
        self.prev = None
        self.cost = Node.grid[x][y][z]
        self.age = 0

    @staticmethod
    def setup_grid(grid):  # set grid and array for monitoring visited nodes
        Node.grid = grid
        Node.visited = [[[0, 0, 0, 0] for i in range(len(grid[0]))] for j in range(len(grid))]

    def is_visited(self):  # return if node has been already visited
        if Node.visited[self.coord[0]][self.coord[1]][self.coord[2]] == 0:
            return False
        else:
            return True

    def get_cost(self, dest):  # return cost of node + manhattans metrics to destination #dest is tuple (x, y)
        a = (self.coord[0], self.coord[1])
        return self.cost + manhattan(a, dest)

    def mark_visited(self):  # mark node as visited
        Node.visited[self.coord[0]][self.coord[1]][self.coord[2]] = self

    def is_dest(self, dest):
        return self.coord[0] == dest[0] and self.coord[1] == dest[1]

    def get_children(self):
        children = []

        tmp_x = self.coord[0] - 1  # search upper child
        tmp_y = self.coord[1]
        tmp_z = BOTTOM
        if tmp_x >= 0:
            tmp_node = Node(tmp_x, tmp_y, tmp_z)
            if not tmp_node.is_visited():
                tmp_node.prev = self.coord
                tmp_node.cost += self.cost
                children.append(tmp_node)

        tmp_x = self.coord[0] + 1  # down child
        tmp_y = self.coord[1]
        tmp_z = UPPER
        if tmp_x < len(Node.grid):
            tmp_node = Node(tmp_x, tmp_y, tmp_z)
            if not tmp_node.is_visited():
                tmp_node.prev = self.coord
                tmp_node.cost += self.cost
                children.append(tmp_node)

        tmp_x = self.coord[0]
        tmp_y = self.coord[1] - 1  # left child
        tmp_z = RIGHT
        if tmp_y >= 0:
            tmp_node = Node(tmp_x, tmp_y, tmp_z)
            if not tmp_node.is_visited():
                tmp_node.prev = self.coord
                tmp_node.cost += self.cost
                children.append(tmp_node)

        tmp_x = self.coord[0]  # right child
        tmp_y = self.coord[1] + 1
        tmp_z = LEFT
        if tmp_y < len(Node.grid[0]):
            tmp_node = Node(tmp_x, tmp_y, tmp_z)
            if not tmp_node.is_visited():
                tmp_node.prev = self.coord
                tmp_node.cost += self.cost
                children.append(tmp_node)

        return children

    def ret_path_prize(self):
        curr = self
        prize = curr.cost
        path = []
        while 1:
            path.append(curr.coord)
            previous = Node.visited[curr.prev[0]][curr.prev[1]][curr.prev[2]]
            if previous.prev is None:
                path.append(previous.coord)
                break
            curr = previous

        return prize, path
