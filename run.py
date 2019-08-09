import os
from collision_metric.scenarios.BasicTCorridorGridScenario import BasicTCorridorGridScenario

if __name__ == "__main__":
    print "Running"
    scenario = BasicTCorridorGridScenario()

    data_file = "./data/BasicTCorridorGridScenario/test_data.txt"
    settings_file = "./data/BasicTCorridorGridScenario/test_settings.txt"
    scenario.load_data(os.path.abspath(data_file), os.path.abspath(settings_file))
    scenario.run_experiment()
    print(scenario.collect_results())
