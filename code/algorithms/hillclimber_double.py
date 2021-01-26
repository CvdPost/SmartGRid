import copy
import random
from code.visualization import visualise
from bokeh.plotting import output_file
# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/hillclimber.py

class HillClimber_double:
    
    def __init__(self, grid):
        if not grid.is_solution():
            raise Exception("HillClimber requires a complete solution.")
        self.grid = copy.deepcopy(grid)
        self.costs = grid.grid_costs()
        self.counter = 1
    def switch_houses_double_swap(self, new_grid):
        random_battery = random.choice(list(new_grid.batteries.values()))
        random_battery_2 = random.choice(list(new_grid.batteries.values()))
        while random_battery == random_battery_2:
            random_battery_2 = random.choice(list(new_grid.batteries.values()))
        # Get a random house from each battery
        house_1 = random.choice(random_battery.connect)
        house_2 = random.choice(random_battery.connect)
        while house_1 == house_2:
            house_2 = random.choice(random_battery.connect)
        output_1_2 = float(house_1.output) + float(house_2.output)
        house_3 = random.choice(random_battery_2.connect)
        house_4 = random.choice(random_battery_2.connect)
        while house_3 == house_4:
            house_4 = random.choice(random_battery_2.connect)
        output_3_4 = float(house_3.output) + float(house_4.output)
        new_battery_output = float(random_battery.total_output) - float(output_1_2) + float(output_3_4)
        new_battery_output_2 = float(random_battery_2.total_output) - float(output_3_4) + float(output_1_2)
        if new_battery_output <= float(random_battery.capacity) and new_battery_output_2 <= float(random_battery.capacity):
            old_distance_1 = self.get_manh_distance(house_1, random_battery) + self.get_manh_distance(house_2, random_battery)
            new_distance_1 = self.get_manh_distance(house_3, random_battery) + self.get_manh_distance(house_4, random_battery)
            old_distance_2 = self.get_manh_distance(house_3, random_battery_2) + self.get_manh_distance(house_4, random_battery_2)
            new_distance_2 = self.get_manh_distance(house_1, random_battery_2) + self.get_manh_distance(house_2, random_battery_2)
            if new_distance_1 <= old_distance_1 and new_distance_2 <= old_distance_2:
                random_battery.disconnect_house(house_1)
                random_battery.disconnect_house(house_2)
                random_battery_2.disconnect_house(house_3)
                random_battery_2.disconnect_house(house_4)
                random_battery.set_connection(house_3)
                random_battery.set_connection(house_4)
                random_battery_2.set_connection(house_1)
                random_battery_2.set_connection(house_2)
                return True
        return False
    def switch_houses_long(self, new_grid):
        battery_list = []
        for battery in new_grid.batteries.values():
            battery_list.append(battery)
        battery_list.sort(key=lambda battery: battery.cable_costs, reverse=True)
        battery_1 = battery_list[0]
        battery_2 = battery_list[1]
        for i in range(len(battery_1.connect)):
            house_1 = battery_1.connect[i]
            for j in range(len(battery_2.connect)):
                house_2 = battery_2.connect[j]
                if self.compare_output(house_1, house_2, battery_1, battery_2):
                    # check if the distances are shorter when houses are swapped
                    if self.compare_distance(house_1, house_2, battery_1, battery_2):
                        battery_1.disconnect_house(house_1)
                        battery_2.disconnect_house(house_2)
                        battery_1.set_connection(house_2)
                        battery_2.set_connection(house_1)
                        return True
        return False
    def compare_output(self, house_1, house_2, battery_1, battery_2):
        '''
        Compares the output value of a battery when houses are swapped.
        Returns True if both batteries don't exceed their capacity (constraint).
        '''
        new_battery_output = float(battery_1.total_output) - float(house_1.output) + float(house_2.output)
        new_battery_output_2 = float(battery_2.total_output) - float(house_2.output) + float(house_1.output)
        if new_battery_output <= float(battery_1.capacity) and new_battery_output_2 <= float(battery_2.capacity):
            return True
        return False
    def compare_distance(self, house_1, house_2, battery_1, battery_2):
        '''
        Compares the manhattan distance betweeen a house and battery before and after swapping.
        If the distance after swap is shorter return true else return false.
        '''
        old_distance_1 = self.get_manh_distance(house_1, battery_1)
        new_distance_1 = self.get_manh_distance(house_1, battery_2)
        old_distance_2 = self.get_manh_distance(house_2, battery_2)
        new_distance_2 = self.get_manh_distance(house_1, battery_2)
        if new_distance_1 <= old_distance_1 and new_distance_2 <= old_distance_2:
            return True
        return False
    def get_manh_distance(self, house, battery):
        '''
        returns the absolute value of the manhattan distance between a house and battery.
        '''
        distance = abs(int(battery.x_location) - int(house.x_location)) + abs(int(battery.y_location) - int(house.y_location))
        return distance
    def check_solution(self, new_grid):
        old_costs = self.costs
        new_costs = new_grid.grid_costs()
        if new_costs < old_costs:
            self.grid = new_grid
            self.costs = new_costs
            # self.grid.output_file(f"testing_output/hill{self.counter}")
            # output_file(f"testing_visual/hill{self.counter}.html")
            # visualise.visualise(self.grid, f"hill{self.counter}")
            self.counter += 1
            print("better solution,", self.costs)
            return True
        return False
    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations
        for iteration in range(iterations):
            # print("current solution", self.costs)
            # print(f'Iteration {iteration}/{iterations}')
            # Create a copy of the graph to simulate the change
            new_grid = copy.deepcopy(self.grid)
            # self.switch_houses(new_grid)
            while self.switch_houses_double_swap(new_grid) != True:
                self.switch_houses_double_swap(new_grid)
            # Accept it if it is better
            if self.check_solution(new_grid) == True:
                print(f'Iteration {iteration}/{iterations}')
        self.grid.output_file('hillclimber_double')