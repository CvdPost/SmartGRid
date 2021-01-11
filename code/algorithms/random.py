import random

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries
    """
    print(grid.batteries.values())
    print(grid.batteries)
    print(list(grid.batteries.values()))

    for house in grid.houses.values():
        battery = random.choice(list(grid.batteries.values()))
        battery.set_connection(house)
    
    # print(battery.connect)
    # print(sum(battery.connect))
        # if sum(battery.connect) > battery.capacity: 
        #     battery.set_connection(house)
        # else:

        