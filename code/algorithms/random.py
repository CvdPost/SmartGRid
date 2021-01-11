import random
import copy

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries
    """
    print(grid.batteries.values())
    print(grid.batteries)
    print(list(grid.batteries.values()))

    #create a copy of grid to remove batteries
    temp_batteries = copy.deepcopy(grid.batteries)
    print('test', temp_batteries)
    

    for house in temp_grid.houses.values():
        battery = random.choice(list(temp_batteries.batteries.values()))
        battery.set_connection(house)

        if sum(battery.connect.values()) > battery.capacity: 

        # for output in house:
  
    # print(battery.connect)
    # print('random')
    # print(battery.connect)
    
 
    # print('hoi', battery.id, sum(battery.connect.values()))
        
            #exclude completed battery in next instance of loop
            completed_battery = battery.id

        #     battery.set_connection(house)
        # else: