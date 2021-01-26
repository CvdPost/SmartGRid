from .depth_first import DepthFirst
import copy


class GreedyLookAhead(DepthFirst):
    """
    A Greedy Look Ahead pruned Depth First algorithm, connecting each house to the closest (i.e. low-cost) battery.
    Almost all of the functions are equal to those of the Depth First class, which is why we use that as a parent class.
    """

    def __init__(self, *args, **kwargs):
        super(GreedyLookAhead, self).__init__(*args, **kwargs)
        self.name = 'GreedyLookAhead'
        self.archived_states = []
        self.failed_paths = []
    
    def build_children(self, grid, house):
        """
        Creates all possible child-states and adds them to the list of states.
        """
    
        # Retrieve all valid possible batteries for the house
        valid_batteries = house.get_possibilities(grid.batteries)

        closest_distance = float('inf')

        print('house.id', house.id)

        # Check if house has a possible battery to connect with
        if len(valid_batteries) == 0:
            
            self.failed_paths.append(grid)
            
            # Find last state in archived states (backtracking)
            grid = self.get_previous_state()

            # Find last unconnected house
            unconnected_house = grid.get_unconnected_house()
            self.build_children(grid, unconnected_house)
        
        else:
            self.archived_states.append(grid)


            # There are still available batteries: Add an instance of the grid to the stack, with a unique battery assigned to each house
            
            best_grid = None
            for valid_battery in valid_batteries:
                new_grid = copy.deepcopy(grid)
                new_grid.batteries[valid_battery.id].set_connection(new_grid.houses[house.id])
                
                # Skip over failed path
                if new_grid in self.failed_paths:
                    continue


                new_house = new_grid.houses[house.id]

                # Check which state has shortest distance house - battery
                if new_house.distance < closest_distance:
                    
                    # Save given grid with short distance
                    best_grid = copy.deepcopy(new_grid)

            # Check if all backtracked paths are failed paths
            if best_grid == None:
                print('test2')
                # Try earlier state
                best_grid = self.get_previous_state()
                
            # Save best state after checking all batteries
            self.states.append(best_grid)

    
    def get_previous_state(self):
        # print('getprevious', self.archived_states.pop())
        return self.archived_states.pop()


    # def build_other_children(self, grid, house, invalid_grid):
    #     """
    #     Creates new possible child-states (of previous grid) and adds them to the list of states, skipping the invalid_grid
    #     """
        
    #     best_grid = None

    #     # Retrieve all valid possible batteries for the house
    #     valid_batteries = house.get_possibilities(grid.batteries)

    #     # Add an instance of the grid to the stack, with a unique battery assigned to each house
    #     for valid_battery in valid_batteries:
            
    #         new_grid = copy.deepcopy(grid)
    #         new_grid.batteries[valid_battery.id].set_connection(new_grid.houses[house.id])

    #         # skip invalid grid:
    #         if new_grid == invalid_grid:
    #             continue
            
    #         new_house = new_grid.houses[house.id]
        
    #         print('valid battery.connect', valid_battery.connect)
    #         print('house distance', new_house.distance)

    #         # Check which state has shortest distance house - battery
    #         if new_house.distance < closest_distance:
                
    #             # Save given grid with short distance
    #             best_grid = copy.deepcopy(new_grid)


         
    #     # If no possible grids available, backtrack again (recursion)
    #     if best_grid = None:

        
    #     # Save best state after checking all batteries
    #     self.states.append(best_grid)

    #     print('no of states', len(self.states))

       
            

    