from collision_metric.state_spaces import StateSpace, State


class Grid4DState(State):
    def __init__(self):
        State.__init__(self)

    def __eq__(self, other):
        pass


class Grid4D(StateSpace):
    def __init__(self):
        StateSpace.__init__(self)

    def get_starting_state(self, source):
        pass

    def set_destination_state(self, destination):
        pass

    def mark_visited(self, start):
        pass

    def expand(self, param):
        pass

    def remake_path(self, curr):
        pass

    def set_data(self, data):
        pass

    def reset(self):
        pass

