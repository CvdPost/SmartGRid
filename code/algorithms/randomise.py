import random
import copy


# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/randomise.py

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries.
    """

    left_overs = []

    for house in grid.houses.values():

        possible_batteries = house.get_possibilities(grid.batteries)
        if len(possible_batteries) != 0:
            battery = random.choice(possible_batteries)
            battery.set_connection(house)
        else:
            left_overs.append(house)

    # Randomize list of left over houses
    random_reassignment(grid, left_overs)
    
    grid.grid_costs()
    grid.output_file('randomise')


def clear_grid(grid):
    """
    Resets the grid for each new instance of Randomise.
    """
    
    for house in grid.houses.values():
        house.set_init()

    for battery in grid.batteries.values():
        battery.set_init()

def random_reassignment(grid, left_overs):
    """
    Runs randomise again for list of leftover houses.
    """
    
    for house in left_overs:
        possible_batteries = house.get_possibilities(grid.batteries)
        if len(possible_batteries) == 0:
            clear_grid(grid)
            random_assignment(grid)
        else: 
            battery = random.choice()
            battery.set_connection(house)
            left_overs.remove(house)
