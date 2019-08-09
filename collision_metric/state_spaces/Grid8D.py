import numpy as np
from collision_metric.state_spaces.StateSpace import StateSpace, State


class Grid8DState(State):
    def __init__(self, x, y, parent_state):
        State.__init__(self)
        self.x = x
        self.y = y
        self.parent = parent_state

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.x == other.x and self.y == other.y


class Grid8D(StateSpace):
    def __init__(self, corridor_width, corridor_height, cell_width, direction_count):
        StateSpace.__init__(self)
        if corridor_width % cell_width != 0 or corridor_height % cell_width != 0:
            raise Exception("Grid would not fit into corridor - dimensions are not divisible by cell width")
        self.width = corridor_width/cell_width
        self.height = corridor_height / cell_width
        self.cell_width = cell_width

        self.data = np.full((self.width, self.height, direction_count), -1.0)
        self.visited = np.full((self.width, self.height), False)
        self.destination = None

    def get_starting_state(self, source):
        return Grid8DState(source[0], source[1], None)

    def set_destination_state(self, destination):
        self.destination = Grid8DState(destination[0], destination[1], None)

    def mark_visited(self, state):
        """
        :type state: Grid8DState
        """
        self.visited[state.x, state.y] = True

    def expand(self, state):
        """

        :type state: Grid8DState
        """
        children = []
        x, y = state.x, state.y
        surroundings = self._get_surroundings(x, y)
        for s, t in surroundings:
            if self.visited[s, t] or self.data[s, t, 0] == -1.0:  # state has been visited or it is a wall
                continue
            else:
                ch = Grid8DState(s, t, state)
                ch.set_cost(self._get_push_cost(s, t, (x, y)))
                children.append(ch)
        return children

    def _get_push_cost(self, x, y, from_direction):
        """
        Function for computing the "resistance measure", a.k.a PUSH

        :param x:  x coord of target cell
        :param y:  y coord of target cell
        :param from_direction: tuple of source cell coords
        :return: cost of taking step into target cell (resistance measure)
        """
        cost = 1.0
        # TODO
        return cost

    def get_pull_traversal_cost(self, x, y, s, t):
        """
        Function for computing the "resistance measure", a.k.a PUSH

        :param x:  x coord of source cell
        :param y:  y coord of source cell
        :param s:  x coord of target cell
        :param t:  y coord of target cell
        :return: cost of taking step into target cell (resistance measure)
        """
        # TODO
        return 1.0

    def _get_surroundings(self, x, y):
        xs = [x + i for i in range(-1, 2)]
        xs = filter(lambda e: not (e >= self.data.shape[0] or e < 0), xs)  # filter positions out of the grid
        ys = [y + i for i in range(-1, 2)]
        ys = filter(lambda e: not (e >= self.data.shape[1] or e < 0), ys)  # filter positions out of the grid
        res = [(s, t) for s in xs for t in ys]  # make permutations
        return filter(lambda (q, w): not (q == x and w == y), res)  # filter no change of pos

    def remake_path(self, curr):
        """

        :type curr: Grid8DState
        """
        path = []
        curr = curr
        while curr.parent is not None:
            path.append((curr.x, curr.y))
            curr = curr.parent
        path.append((curr.x, curr.y))
        path.reverse()
        return path

    def set_data(self, data):
        if isinstance(data, type(np.array())) and data.shape == self.data.shape:
            self.data = data
        else:
            data = np.asarray(data)
            if data.shape == self.data.shape:
                self.data = data
            else:
                raise Exception("Unsupported data format for grid")

    def set_location_direction_value(self, x, y, direction, value):
        if x > self.data.shape[0] or \
                y > self.data.shape[1] or \
                direction > self.data.shape[2]:
            raise Exception("Out of bounds of grid")
        self.data[x, y, direction] = value

    def set_location_values(self, x, y, values):
        if x > self.data.shape[0] or \
                y > self.data.shape[1] or \
                len(values) != self.data.shape[2]:
            raise Exception("Out of bounds of grid")
        self.data[x, y, :] = values

    def set_grid_to_value(self, value):
        self.data.fill(value)

    def draw_wall(self, position, direction, length):
        if length % self.cell_width:
            raise Exception("Wall would not fit into the grid - it's length is not divisible by cell width")
        n_cells = length/self.cell_width

        for i in range(n_cells):
            self.data[position[0] + i * direction[0], position[1] + i * direction[1], 0] = -1.0

    def reset(self):
        self.data = np.full(self.data.shape, -1.0)
        self.visited = np.full(self.data.shape[:-1], False)
        self.destination = None

    def __str__(self):
        ret = ""
        for i in range(self.width):
            for j in range(self.height):
                ret += "{0} ".format(self.data[i, j])
            ret += "\n"
        return ret
