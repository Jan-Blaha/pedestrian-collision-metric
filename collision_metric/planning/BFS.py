import heapq
from collision_metric.state_spaces.StateSpace import StateSpace


class BFS:
    space = None  # type: StateSpace

    def __init__(self, state_space=None):
        if state_space is None or issubclass(type(state_space), StateSpace):
            raise Exception("No or invalid state space specified.")

        self.space = state_space

    def set_data(self, data):
        self.space.set_data(data)

    # MAIN SEARCH ALGORITHM
    def search(self, source, destination):
        queue = []
        heapq.heapify(queue)

        start = self.space.get_starting_state(source)
        dest = self.space.set_destination_state(destination)

        heapq.heappush(queue, (0, 0, start))
        self.space.mark_visited(start)

        curr = start
        while len(queue) > 0:
            curr = heapq.heappop(queue)

            if curr[2] == dest:
                break

            children = self.space.expand(curr[2])
            for i in range(len(children)):
                heapq.heappush(queue, (children[i].get_cost() + curr[0], curr[1] + 1, children[i]))
                self.space.mark_visited(children[i])

        return self.space.remake_path(curr[2])



