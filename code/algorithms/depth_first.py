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

    def get_next_state(self):
        return self.states.pop()

    def build_children(self, grid, house):
        """
        Creates all possible child-states and adds them to the list of states.
        """
        # Retrieve all valid possible batteries for the house.
        valid_batteries = house.get_possibilities(grid.batteries)

        # Add an instance of the grid to the stack, with a unique battery assigned to each house
        for valid_battery in valid_batteries:
            new_grid = copy.deepcopy(grid)
            new_grid.batteries[valid_battery.id].set_connection(house) 
            self.states.append(new_grid)

        print('states', len(self.states))


    def check_solution(self, new_grid):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_costs = new_grid.grid_costs() #or use grid_costs()?
        old_costs = self.best_costs
        print('old',old_costs)
        print('new',new_costs)

        #Looking for lower costs, so:
        if new_costs <= old_costs:
            self.best_solution = new_grid
            self.best_costs = new_costs
            print(f"New best costs: {self.best_costs}")
    
    def run(self):
        """
        Runs the algorithm until all possible states are visisted.
        """
        while self.states:
            new_grid = self.get_next_state()

            house = new_grid.get_unconnected_house()

            if house is not None:
                self.build_children(new_grid, house)
            else:
                # Stop if we find a solution
                # break

                # or continue looking for better graph
                self.check_solution(new_grid)
        
        # Update the input graph with the best result found.
        self.grid = self.best_costs


            





