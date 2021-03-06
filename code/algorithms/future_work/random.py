import random
import copy


# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/randomise.py

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries
    """

    for house in grid.houses.values():
        house.set_init()

    for battery in grid.batteries.values():
        battery.set_init()

    
    left_overs = []

    for house in grid.houses.values():

        house.get_possibilities(grid.batteries)
        battery = random.choice(list(grid.batteries.values()))

        # compare total output + new house output with total capacity battery.
        # append to list if not house not assigned to battery
        new_output = battery.total_output + float(house.output)
        
        if new_output >= float(battery.capacity):
            left_overs.append(house)
        else:
            battery.set_connection(house)

    reassigned_houses = []

    # reassigning left over houses.
    for house in left_overs:
        for battery in grid.batteries.values():
            new_output = battery.total_output + float(house.output)
            
            # if new_output smaller than capacity add house to reassigned list and break out.
            if new_output < float(battery.capacity):
                battery.set_connection(house)
                reassigned_houses.append(house)
                break

    # check if list left_overs and reassigned_houses same lenght, if so: there is a solution.
    remaining = len(left_overs) - len(reassigned_houses)
    
    if remaining == 0:
        return True
    else:
        return False


        