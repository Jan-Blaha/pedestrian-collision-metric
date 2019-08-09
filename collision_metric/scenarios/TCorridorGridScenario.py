import json
from collision_metric.planning.BFS import BFS
from collision_metric.scenarios.Scenario import Scenario
from collision_metric.state_spaces.Grid8D import Grid8D


class TCorridorGridScenario(Scenario):
    # == EXPERIMENT SET UP ==

    # cell width for fineness settings
    cell_width = 1

    # width & height of corridor the unit of length is arbitrary, but should be the same for w and h
    corridor_width = 3  # 20 * 100
    corridor_height = 4  # 20 * 100

    # list of walls in format - (starting_position, direction_vector, length)
    walls = [
        ((0, 0), (1, 0), 2),  # from top-left corner two units of length down
        ((0, 2), (1, 0), 2),  # from top-right corner two units of length down
        ((3, 0), (0, 1), 3)  # from down-left corner three units of length left
    ]

    # number of how many directions will have assigned number from model
    direction_count = 4

    # == / EXPERIMENT SET UP ==

    def __init__(self):
        Scenario.__init__(self)
        self.grid = Grid8D(
            corridor_width=self.corridor_width,
            corridor_height=self.corridor_height,
            cell_width=self.cell_width,
            direction_count=self.direction_count
        )
        self.result_trajectory = []
        self.path = []

    def run_experiment(self):
        pass

    def collect_results(self):
        pass

    @staticmethod
    def _path_planning(grid, start, target):
        planner = BFS(grid)
        return planner.search(start, target)

    @staticmethod
    def _velocity_profile(grid, path):
        """
        Function that transforms self.path variable (list of positions) into trajectory.
        :return:
        """
        # TODO
        # sketch how it should be done, more or less:

        trajectory = []
        prev_x, prev_y = path[0]
        time = 0
        for x, y in path[1:]:
            # get cost of transition regarding the PULL factor of pedestrian flow
            cost = grid.get_pull_traversal_cost(prev_x, prev_y, x, y)

            # euclidean distance
            distance = ((prev_x - x) ** 2) + ((prev_y - y) ** 2) ** 0.5

            # if cost is equal to ideal velocity
            time += distance / cost
            trajectory.append(
                ((x, y), time)
            )

        return trajectory

    def load_data(self, data, experimental_settings= None):
        if experimental_settings is not None:
            if isinstance(experimental_settings, type(dict())):
                self._load_settings_dict(experimental_settings)
            if isinstance(experimental_settings, type(str())):
                self._load_settings_path(experimental_settings)
        if isinstance(data, type(list())):
            self._load_data_list(data)
        if isinstance(data, type(str())):
            self._load_data_path(data)

    def _load_settings_dict(self, settings):
        self.corridor_height = settings["corridor_height"]
        self.corridor_width = settings["corridor_width"]
        self.cell_width = settings["cell_width"]
        self.walls = settings["walls"]
        self.direction_count = settings["direction_count"]
        self.grid = Grid8D(
            corridor_width=self.corridor_width,
            corridor_height=self.corridor_height,
            cell_width=self.cell_width,
            direction_count=self.direction_count
        )

    def _load_settings_path(self, path):
        with open(path, 'r') as f:
            settings = json.load(f)
        self._load_settings_dict(settings)

    def _load_data_list(self, data):
        pass

    def _load_data_path(self, path):
        pass

    @staticmethod
    def _count_collisions(trajectory, pedestrian_trajectories):
        """
        Function for computing the metric of collisions,
        it should get data of how pedestrians were moving,
        then compute the metric against prepared trajectory
        and return number.

        :return: number of collisions 
        """""
        # TODO
        return 1
