import copy
import random


# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/hillclimber.py
class HillClimber:  

    def __init__(self, grid):
        if not grid.is_solution():
            raise Exception("HillClimber requires a complete solution.")

        self.grid = copy.deepcopy(grid)
        self.costs = grid.grid_costs()

    def switch_houses(self, grid):
        random_battery = random.choice(list(grid.batteries.values())) 
        random_battery_2 = random.choice(list(grid.batteries.values()))

        while random_battery == random_battery_2:
            random_battery_2 = random.choice(list(grid.batteries.values()))

        random_house = random.choice(random_battery.connect)
        random_house_2 = random.choice(random_battery_2.connect) 

        # calculates new output of batteries when houses are switched
        new_battery_output = float(random_battery.total_output) - float(random_house.output) + float(random_house_2.output)
        new_battery_output_2 = float(random_battery_2.total_output) - float(random_house_2.output) + float(random_house.output)
    
        # checks if new output of batteries meets constraint
        if new_battery_output <= float(random_battery.capacity) and new_battery_output_2 <= float(random_battery_2.capacity):

            # calculates distances to battery when houses are switched 
            old_distance = abs(int(random_battery.x_location) - int(random_house.x_location)) + abs(int(random_battery.y_location) - int(random_house.y_location))
            new_distance = abs(int(random_battery_2.x_location) - int(random_house.x_location)) + abs(int(random_battery_2.y_location) - int(random_house.y_location))

            old_distance_2 = abs(int(random_battery_2.x_location) - int(random_house_2.x_location)) + abs(int(random_battery_2.y_location) - int(random_house_2.y_location))
            new_distance_2 = abs(int(random_battery.x_location) - int(random_house_2.x_location)) + abs(int(random_battery.y_location) - int(random_house_2.y_location))

            # checks if new location house is closer to new battery compared to old situation 
            if new_distance <= old_distance and new_distance_2 <= old_distance_2:
                random_battery.disconnect_house(random_house)
                random_battery_2.disconnect_house(random_house_2)
                random_battery.set_connection(random_house_2)
                random_battery_2.set_connection(random_house)
        


    def check_solution(self, new_grid):

        old_costs = self.costs
        new_costs = new_grid.grid_costs()

        if new_costs < old_costs:
            self.grid = new_grid
            self.costs = new_costs
            print("better solution,", self.costs)
        else: 
            print("no better solution")

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            print("current solution", self.costs)
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}')

            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)

            self.switch_houses(new_grid)

            # Accept it if it is better
            self.check_solution(new_grid)

        self.grid.output_file('hillclimber')












    


