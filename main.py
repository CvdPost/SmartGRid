from code.classes import grid, house
from code.visualization import visualise

from code.algorithms import random, depth_first, breadth_first, randomise

from bokeh.models import grids
from bokeh.plotting import figure, output_file, show
import time


 

if __name__ == "__main__":

    print('Welcome to Smartsplitters Smartgrid algorithm!')
    print('=================================================')
    print()
    
    # List of available districts, add any new districts manually if added
    districts = ['0', '1', '2', '3']
    print('District Choices:')
    print('-------------------------------------------------')
    for item in districts:
        print(item)
    print('-------------------------------------------------')

    print('For what district would you like to run an algorithm?')
    district = input()
    while district not in districts:
        print('Please choose an avaible district.')
        district = input()
    print('=================================================')
    print()

    # List of available algorithms, add any new made algoritms manually
    algorithms = ['random', 'randomise', 'depth_first', 'breadth_first']
    print('Available algorithms:')
    print('-------------------------------------------------')
    for item in algorithms:
        print(item)
    print('-------------------------------------------------')

    print('What algorithm would you like to use? ')
    algorithm = input()
    while algorithm.lower() not in algorithms:
        print('Please choose an algorithm from the available options.')
        print('Please make sure the input matches the available options.')
        algorithm = input()
    print('=================================================')

    # input('Would you like a visualisation of the output? Y/N')

    print(f"running {algorithm} algorithm with district {district}...")
    
    # Start running time
    start_time = time.time()

    # choose which data folder we pick
    data_folder = f"district_{district}"

    # choose the data file name
    data_file = f"district-{district}"

    # Create a grid from our data
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv", data_folder)
    
    # ------------------------------ RANDOM ---------------------------------- #
    if algorithm == 'random':
        while random.random_assignment(test_grid) == False:
            random.random_assignment(test_grid)
        # calculates total costs and generates output file
        test_grid.grid_costs()
        test_grid.output_file(algorithm)
    
    # ------------------------------ DEPTH FIRST ------------------------------ #
    elif algorithm == 'depth_first':
        depth = depth_first.DepthFirst(test_grid)
        depth.run()
    # print('best sol', depth.best_solution)
    # print('best costs', depth.best_costs)
     
    # ------------------------------ BREADTH FIRST ------------------------------ #
    elif algorithm == 'breadth_first':
        breadth = breadth_first.BreadthFirst(test_grid)
        breadth.run()
    # print('best sol', breadth.best_solution)
    # print('best costs', breadth.best_costs)

    # ------------------------------ RANDOMISE ---------------------------------- #
    elif algorithm == 'randomise':
        randomise.randomise(test_grid)

    #Creating a visualisation
    output_file(f"{data_folder}.html")

    # visualise.visualise(test_grid, data_folder)
    
    print(f"output file created in {algorithm}-data.json")

    # running time
    print("--- %s seconds ---" % (time.time() - start_time))

    