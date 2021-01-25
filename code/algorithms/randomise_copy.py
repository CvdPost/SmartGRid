import random
import copy
import time


# Based on: https://github.com/minprog/radio_russia_demo/blob/college_2/code/algorithms/randomise.py
def randomise(grid, end_time):
    """
    Keep running while houses are not all connected.
    """
    running_time = 0
    start = time.time()
    total_runs = 0
    no_solutions = 0 
    avg_runs = 0
    best_grid = None

    while running_time < end_time:
        runs = 1
        while random_assignment(grid) == False:
            random_assignment(grid)
            total_runs += 1
            runs += 1
        no_solutions += 1
        
        if best_grid == None:
            # print('calculating costs')
            best_grid = copy.deepcopy(grid)
            best_grid.grid_costs()
        elif grid.grid_costs() < best_grid.total_costs:
            best_grid = copy.deepcopy(grid)


        print('generating ouput .json')
        best_grid.output_file('randomise')

        print(f"times randomise ran to find a solution: {runs}")
        running_time = time.time() - start
    avg_runs = total_runs / no_solutions
    print('Average amount of runs to find solution: ', avg_runs)

def check_solution(grid, best_costs):
    new_solution = grid.costs()

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries.
    """
    clear_grid(grid)
    left_overs = []

    for house in grid.houses.values():

        possible_batteries = house.get_possibilities(grid.batteries)
        if len(possible_batteries) != 0:
            battery = random.choice(possible_batteries)
            battery.set_connection(house)
        else:
            left_overs.append(house)

    if random_reassignment(grid, left_overs):
        return True
    return False

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
            return False
        else:  
            battery = random.choice()
            battery.set_connection(house)
            left_overs.remove(house)

    return True


