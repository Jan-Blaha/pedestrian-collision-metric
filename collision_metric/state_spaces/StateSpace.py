import abc


class State:
    def __init__(self):
        self.cost = 0
        pass

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    @abc.abstractmethod
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        return not self.__eq__(other)


class StateSpace:
    def __init__(self):
        pass

    @abc.abstractmethod
    def set_data(self, data):
        pass

    @abc.abstractmethod
    def get_starting_state(self, source):
        pass

    @abc.abstractmethod
    def set_destination_state(self, destination):
        pass

    @abc.abstractmethod
    def mark_visited(self, start):
        pass

    @abc.abstractmethod
    def expand(self, param):
        pass

    @abc.abstractmethod
    def remake_path(self, curr):
        pass

    @abc.abstractmethod
    def reset(self):
        pass
