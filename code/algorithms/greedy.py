from .depth_first import DepthFirst
import copy


class GreedyLookAhead(DepthFirst):
    """
    A Greedy Look Ahead Depth First algorithm, connecting each house to the closest (i.e. low-cost) battery.
    Almost all of the functions are equal to those of the Depth First class, which is why we use that as a parent class.
    """

    def __init__(self, *args, **kwargs):
        super(GreedyLookAhead, self).__init__(*args, **kwargs)
        self.name = 'GreedyLookAhead'
    

    def build_children(self, grid, house):
        """
        Creates all possible child-states and adds them to the list of states.
        """

        archived_states = []
        # Retrieve all valid possible batteries for the house
        valid_batteries = house.get_possibilities(grid.batteries)

        # Add an instance of the grid to the stack, with a unique battery assigned to each house
        for valid_battery in valid_batteries:
            new_grid = copy.deepcopy(grid)
            new_grid.batteries[valid_battery.id].set_connection(new_grid.houses[house.id])
            
            # put the children state in a list
            archived_states.append(new_grid)
            
            # Sort the children states by distance (larger to smaller) from the connected house to the battery
            archived_states.sort(key=lambda new_grid: new_grid.houses[house.id].distance, reverse=True)

        # add the children states to the list of states such that the furthest battery is added first
        for state in archived_states:    
            self.states.append(state)
 
            
