from .depth_first import DepthFirst
import copy


class Greedy(DepthFirst):
    """
    A Greedy Depth First algorithm, connecting each house to the closest (i.e. low-cost) battery.
    Most functions are equal to the Depth First class, therefore we inherit from Depth First.
    """

    def __init__(self, *args, **kwargs):
        super(Greedy, self).__init__(*args, **kwargs)
        self.name = 'Greedy'
    

    def build_children(self, grid, house):
        """
        Creates all possible child-states and adds them to the list of states.
        These child-states are reverse sorted by distance.
        """

        archived_states = []

        # Retrieve all valid possible batteries for the house
        valid_batteries = house.get_possibilities(grid.batteries)

        # Add an instance of the grid to the stack, with a unique battery assigned to each house
        for valid_battery in valid_batteries:
            new_grid = copy.deepcopy(grid)
            new_grid.batteries[valid_battery.id].set_connection(new_grid.houses[house.id])
            
            # Put the child state in a list
            archived_states.append(new_grid)
            
            # Reverse sort of child states by distance between the house and battery
            archived_states.sort(key=lambda new_grid: new_grid.houses[house.id].distance, reverse=True)

        # Add the child states to the list of states such that the furthest battery is added first
        for state in archived_states:    
            self.states.append(state)
 
            
