from code.visualization import visualise
import copy

# Based on https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/depth_first.py
class DepthFirst:
    """
    A Depth First algorithm that builds a stack of grids with a unique distribution of battery connections
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [copy.deepcopy(self.grid)]
        self.best_solution = None
        self.best_costs = float('inf')
        self.name = 'Depth_first'

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
        Checks and accepts better solutions than the current solution.
        """

        new_costs = new_grid.grid_costs()
        old_costs = self.best_costs

        # checking for new best costs
        if new_costs < old_costs:
            self.best_solution = new_grid
            self.best_costs = new_costs
            print(f"New best costs: {self.best_costs}")
            new_grid.output_file(self.name)
            visualise.visualise(new_grid, self.name)
            # input()
        else:
            print('no better cost found')
    
    def run(self):
        """
        Runs the algorithm until all possible states are visisted.
        """
        
        while self.states:
            new_grid = self.get_next_state()
            house = new_grid.get_unconnected_house()

            # if all houses have a connection -> check solution 
            if house is not None:
                self.build_children(new_grid, house)
            else:
                self.check_solution(new_grid)
                
        # Update the input graph with the best result found.
        self.grid = self.best_solution
        print('result', self.best_solution)


            





