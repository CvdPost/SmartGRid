from code.classes import grid, house
from code.visualization import visualise

from code.algorithms import random

from bokeh.models import grids
from bokeh.plotting import figure, output_file, show

import json

if __name__ == "__main__":

    # choose which data folder we pick
    data_folder = "district_1"

    # choose the data file name
    data_file = "district-1"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv", data_folder)
    
    #Randomly assign a house to one of the batteries
    random.random_assignment(test_grid)
    b_list = test_grid.batteries[1]

    #Creating a visualisation
    output_file(f"{data_folder}.html")

    # visualise.visualise(test_grid, data_folder)

    for battery in test_grid.batteries.values():
        for house in battery.connect:
            distance = house.manhattan_distance(battery, house)
            cost = house.cable_costs_house(distance)
    
    test_grid.grid_costs()

    
    
    #Creating an output file      
    data = {}
    
    data[0] = []
    # For only one district (add loop when analyzing multiple districts)
    data[0].append({
        'district': test_grid.name,
        'costs-shared': test_grid.total_costs
    })
    i = 1
    for i, battery in enumerate(test_grid.batteries.values()):
        data[i] = []
        data[i].append({
        'location': f"{battery.x_location}, {battery.y_location}",
        'capacity': battery.capacity,
        'houses': 
        for house in battery.connect.values():
            data_houses['house'] = []
            data_houses['house'].append({
                'location': f"{house.x_location}, {house.y_location}"
                })

        })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


    # {test_grid['district'] = test_grid.name, test_grid['costs-shared'] = None}
    # # Iterate over batteries
    # while i != len(test_grid.batteries)
    
    #     for battery in test_grid.batteries:
    #         location = f"{battery.x_location}, {battery.y_location}"
    #         data[battery.id] = {'location' = location
            
            
            
    #         {test_grid['location'] = test_grid.}

    # data['costs-shared'] = None
    # data['location'] = battery.x_location, battery.y_location
    # data['capacity'] = 
    # data['houses'] = 
