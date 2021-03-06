from code.visualization import visualise
import copy
import time

# Based on https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/depth_first.py


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of grids with a unique distribution of battery connections.
    """
    
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.best_solution = None
        self.best_costs = float('inf')
        self.name = 'Depth_first'
        self.running_time = 0
        self.start = time.time()


    def get_next_state(self):
        """
        Pops last element of stack.
        """

        return self.states.pop()


    def build_children(self, grid, house):
        """
        Creates all possible child-states and adds them to the list of states.
        """
        
        # Retrieve all valid possible batteries for the house
        valid_batteries = house.get_possibilities(grid.batteries)

        # Add an instance of the grid to the stack, with a unique battery assigned to each house
        for valid_battery in valid_batteries:
            new_grid = copy.deepcopy(grid)
            new_grid.batteries[valid_battery.id].set_connection(new_grid.houses[house.id])
            self.states.append(new_grid)


    def check_solution(self, new_grid):
        """
        Checks and updates the grid and costs attribute if a better solution is found.
        """

        new_costs = new_grid.grid_costs()
        old_costs = self.best_costs

        # Checking for new best costs
        if new_costs < old_costs:
            self.best_solution = new_grid
            self.best_costs = new_costs
            print(f"New best costs: {self.best_costs}")
    

    def run(self, end_time):
        """
        Runs the algorithm until all possible states are visisted.
        """

        while self.states and self.running_time <= end_time:
            new_grid = self.get_next_state()
            house = new_grid.get_unconnected_house()
            
            # If all houses have a connection -> check solution 
            if house is not None:
                self.build_children(new_grid, house)
            else:
                self.check_solution(new_grid)
            
            self.running_time = time.time() - self.start

        # Update the input graph with the best result found.
        self.grid = self.best_solution
        self.grid.output_file(self.name)


