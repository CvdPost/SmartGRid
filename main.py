from code.classes import grid
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

    visualise.visualise(test_grid, data_folder)

    solution_file = dictwriter("poep")

    data = {}
    data['0'] = grid.name
    data['costs-shared'] = None
    data['location']
