import random

def random_assignment(grid, houses):
    """
    Randomly assign each house to one of the batteries
    """
    for battery in grid.batteries.values():
        battery.set_connection(random.choice(grid.houses))
        