from collision_metric.data_extraction.GridDataParser import GridDataParser
from collision_metric.scenarios.TCorridorGridScenario import TCorridorGridScenario


class BasicTCorridorGridScenario(TCorridorGridScenario):
    """
    Experimental setup should only be modified through load_data !!
    Setting already present are proof of concept for the following set up:
             _________________
            |  W  |     |  W  |
            |_____|_____|_____|         where W stands for wall, S for start, T for target,
            |  W  |     |  W  |             every field is valued by one number and cell width is unitary
            |_____|_____|_____|
            |  S  |     |  T  |
            |_____|_____|_____|
            |  W  |  W  |  W  |
            |_____|_____|_____|


    """

    # == EXPERIMENT SET UP ==

    # starting position coords
    starting_position = (2, 0)

    # target position coords
    target_position = (2, 2)

    # == / EXPERIMENT SET UP ==

    def __init__(self):
        TCorridorGridScenario.__init__(self)

    def run_experiment(self):
        # make walls, this should be done after inserting data as a security measure against adversary input
        for position, direction, length in self.walls:
            self.grid.draw_wall(position, direction, length)

        # path planning phase
        self.path = self._path_planning(self.grid, self.starting_position, self.target_position)

        # creating trajectory phase
        self.result_trajectory = self._velocity_profile(self.grid, self.path)

    def collect_results(self):
        # TODO: get trajectories from somewhere
        pedestrian_trajectories = []
        return self._count_collisions(self.result_trajectory, pedestrian_trajectories)

    def _load_settings_dict(self, settings):
        super(BasicTCorridorGridScenario, self)._load_settings_dict(settings)
        self.starting_position = settings["starting_position"]
        self.target_position = settings["target_position"]

    def _load_data_list(self, data):
        pass

    def _load_data_path(self, path):
        parser = GridDataParser(path)
        for (x, y), values in parser.generator():
            self.grid.set_location_values(x, y, values)

    def get_needed_positions(self):
        """
        This function should be used for generating list of positions,
        that will be needed from other teams to evaluate.

        :return:
        """
        # TODO
        # challenge will be to derive this list given only info about the walls

        return [
            (0, 0)
        ]
