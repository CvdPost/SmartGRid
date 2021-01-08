from code.classes import grid

from code.algorithms import random

from bokeh.models import grids
from bokeh.plotting import figure, output_file, show

import matplotlib.pyplot as plt
import networkx as nx

if __name__ == "__main__":

    # choose which data folder we pick
    data_folder = "district_1"

    # choose the data file name
    data_file = "district-1"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv")
    
    #Randomly assign a house to one of the batteries
    random.random_assignment(test_grid)
    b_list = test_grid.batteries[1]

    #Creating a visualisation
    output_file("test.html")

    p = figure(plot_width=400, plot_height=400)
    
    # Plotting the batteries  (navy blue)
    for battery in test_grid.batteries.values():
        print(battery.x_location, battery.y_location)
        p.circle([battery.x_location], [battery.y_location], size=20, color="navy", alpha=1)
    
    # Plotting the houses  (red)
    for house in test_grid.houses.values():
        p.circle([house.x_location], [house.y_location], size=7, color="red", alpha=0.5)
    
    
    show(p)






    