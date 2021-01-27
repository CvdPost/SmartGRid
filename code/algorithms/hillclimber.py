import copy
import random

from code.visualization import visualise
from bokeh.plotting import output_file

# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/hillclimber.py


class HillClimber:
    """
    Hillclimber starts with a feasible grid and tries to improve that grid by randomly switching two houses.
    """

    def __init__(self, grid):
        if not grid.is_solution():
            raise Exception("HillClimber requires a complete solution.")

        self.grid = copy.deepcopy(grid)
        self.costs = grid.grid_costs()


    def switch_houses(self, new_grid):
        """
        This method randomly retrieves two batteries. From each battery it also randomly retrieves one house.
        If a switch is successful the houses are switched and this method returns True.
        """

        # Get two unique random batteries
        random_battery = random.choice(list(new_grid.batteries.values())) 
        random_battery_2 = random.choice(list(new_grid.batteries.values()))

        while random_battery == random_battery_2:
            random_battery_2 = random.choice(list(new_grid.batteries.values()))

        # Get a random house from each battery
        random_house = random.choice(random_battery.connect)
        random_house_2 = random.choice(random_battery_2.connect)
       
        # Check if switching houses doesn't exceed battery capacity constraint
        if self.compare_output(random_house, random_house_2, random_battery, random_battery_2):
            
            # Check if switching houses results in shorter distances
            if self.compare_distance(random_house, random_house_2, random_battery, random_battery_2):
                
                # Switch houses
                random_battery.disconnect_house(random_house)
                random_battery_2.disconnect_house(random_house_2)
            
                random_battery.set_connection(random_house_2)
                random_battery_2.set_connection(random_house)
                return True
        return False
  

    def compare_output(self, house_1, house_2, battery_1, battery_2):
        """
        Compares the old output value of a battery to the post switch output.
        Returns True if both batteries don't exceed their capacity.
        """

        new_battery_output = float(battery_1.total_output) - float(house_1.output) + float(house_2.output)
        new_battery_output_2 = float(battery_2.total_output) - float(house_2.output) + float(house_1.output)

        if new_battery_output <= float(battery_1.capacity) and new_battery_output_2 <= float(battery_2.capacity):
            return True
        return False


    def compare_distance(self, house_1, house_2, battery_1, battery_2):
        """
        Compares the manhattan distance between a house and battery before and after switching.
        If the distance after switch is shorter it returns True, else it returns False.
        """

        old_distance_1 = self.get_manh_distance(house_1, battery_1)
        new_distance_1 = self.get_manh_distance(house_1, battery_2)

        old_distance_2 = self.get_manh_distance(house_2, battery_2)
        new_distance_2 = self.get_manh_distance(house_1, battery_2)

        if new_distance_1 <= old_distance_1 and new_distance_2 <= old_distance_2: 
            return True
        return False


    def get_manh_distance(self, house, battery):
        '''
        Returns the absolute manhattan distance between a house and a battery.
        '''

        distance = abs(int(battery.x_location) - int(house.x_location)) + abs(int(battery.y_location) - int(house.y_location))
        return distance


    def check_solution(self, new_grid):
        """
        Checks and updates the grid and costs attribute if a better solution is found.
        """

        old_costs = self.costs
        new_costs = new_grid.grid_costs()
        
        if new_costs < old_costs:
            self.grid = new_grid
            self.costs = new_costs
            print("better solution,", self.costs)
            return True

        return False


    def run(self, iterations):
        """
        Runs the Hillclimber algorithm for a specific number of iterations.
        """

        self.iterations = iterations

        for iteration in range(iterations):
            new_grid = copy.deepcopy(self.grid)
            while self.switch_houses(new_grid) != True:
                self.switch_houses(new_grid)

            # Accepts solution if better than previous
            if self.check_solution(new_grid) == True:
                print(f'Iteration {iteration}/{iterations}')
            
        self.grid.output_file('hillclimber')


