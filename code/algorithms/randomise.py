import random
import copy


# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/randomise.py

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries.
    """
    left_overs = []

    for house in grid.houses.values():

        house.get_possibilities(grid.batteries)
        battery = random.choice(list(grid.batteries.values()))

        # compare total output + new house output with total capacity battery.
        # append to list if not house not assigned to battery
        new_output = battery.total_output + float(house.output)
        # print(f"new output: {new_output}, battery capacity: {battery.capacity}")
        if new_output >= float(battery.capacity):
            left_overs.append(house)
        else:
            battery.set_connection(house)
        
    # Randomize list of left over houses
    random_reassignment(left_overs)


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
        battery = random.choice(list(grid.batteries.values()))
        new_output = battery.total_output + float(house.output)
        if new_output >= float(battery.capacity):
            continue
        else:
            battery.set_connection(house)
            left_overs.remove(house)
    


