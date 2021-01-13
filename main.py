from code.classes import grid, house
from code.visualization import visualise

from code.algorithms import random

from bokeh.models import grids
from bokeh.plotting import figure, output_file, show
import time

start_time = time.time()
 

if __name__ == "__main__":

    # choose which data folder we pick
    data_folder = "district_1"

    # choose the data file name
    data_file = "district-1"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv", data_folder)
    
    #Randomly assign a house to one of the batteries
    # test1 = random.random_assignment(test_grid)
   
    while random.random_assignment(test_grid) == False:
        print("LOSERS", test_grid.total_costs)
        random.random_assignment(test_grid)

   
    #Creating a visualisation
    output_file(f"{data_folder}.html")

    # visualise.visualise(test_grid, data_folder)

    # calculates total costs and gerenarest output file
    test_grid.grid_costs()
    test_grid.output_file()
    print("SOLUTION")
    print("--- %s seconds ---" % (time.time() - start_time))

    