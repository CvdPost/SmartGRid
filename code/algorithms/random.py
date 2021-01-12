import random
import copy

# from code.classes import battery as bat

def random_assignment(grid):
    """
    Randomly assign each house to one of the batteries
    """
    print(grid.batteries.values())
    print(grid.batteries)
    print(list(grid.batteries.values()))

    #create a copy of grid to remove batteries
    # temp_batteries = copy.deepcopy(grid.batteries)
    # print('test', temp_batteries)
    
    left_overs = []
    for house in grid.houses.values():
        battery = random.choice(list(grid.batteries.values()))
    
        new_output = battery.total_output + float(house.output)
        print('new:', battery.id, new_output)
        if new_output >= float(battery.capacity):
            left_overs.append(house)
        else:
            battery.connected_output(house)
            battery.set_connection(house)

    print('haai', battery.id, battery.total_output)
    print(left_overs)

    # reasigning left over houses
    for house in left_overs:
        # left_overs.remove(house)
        for battery in grid.batteries.values():
        # battery = random.choice(list(grid.batteries.values()))
    
            new_output = battery.total_output + float(house.output)
            print('new2:', battery.id, new_output)
            if new_output >= float(battery.capacity):
                print('left over:', house.id, house.output)
                # left_overs.append(house)
            else:
                battery.connected_output(house)
                battery.set_connection(house)
                # left_overs.remove(house)
    
    print('last:', left_overs)
    print('haai2', battery.id, battery.total_output)
    
        

        # if sum(battery.connect.values()) > battery.capacity: 

        # for output in house:
  
    # print(battery.connect)
    # print('random')
    # print(battery.connect)
    
 
    # print('hoi', battery.id, sum(battery.connect.values()))
        
            #exclude completed battery in next instance of loop
            # completed_battery = battery.id

        #     battery.set_connection(house)
        # else: