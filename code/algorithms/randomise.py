import random
import copy


# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/randomise.py

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries.
    """
    print('!!start!!')
    print('***************************')
    left_overs = []

    for house in grid.houses.values():

        possible_batteries = house.get_possibilities(grid.batteries)
        if len(possible_batteries) != 0:
            battery = random.choice(possible_batteries)
            battery.set_connection(house)
        else:
            left_overs.append(house)


        # compare total output + new house output with total capacity battery.
        # append to list if not house not assigned to battery
        # new_output = battery.total_output + float(house.output)
        # # print(f"new output: {new_output}, battery capacity: {battery.capacity}")
        # if new_output >= float(battery.capacity):
        #     left_overs.append(house)
        # else:
        #     battery.set_connection(house)
        
    # Randomize list of left over houses
    print(left_overs)
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
    # print('houses for reassign:', left_overs)
    for house in left_overs:
        # print(house)
        # input()
        possible_batteries = house.get_possibilities(grid.batteries)
        # print('number of batteries:', len(possible_batteries), possible_batteries)
        if len(possible_batteries) == 0:
            clear_grid(grid)
            # print('restart!')
            # input()
            random_assignment(grid)
        else:
            # print('assigned house')    
            battery = random.choice()
            battery.set_connection(house)
            left_overs.remove(house)




        # new_output = battery.total_output + float(house.output)
        # if new_output >= float(battery.capacity):
        #     continue
        # else:
        #     battery.set_connection(house)
        #     left_overs.remove(house)
    

