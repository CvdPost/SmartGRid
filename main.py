from code.classes import grid, house
from code.visualization import visualise

from code.algorithms import random, depth_first, breadth_first, randomise, hillclimber

from bokeh.models import grids
from bokeh.plotting import figure, output_file, show
import time

import math

from datetime import datetime





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
    algorithms = ['random', 'randomise', 'depth_first', 'breadth_first', 'hillclimber']
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

    running_time = input("How many hours do you want the program to run? ")
    running_time = float(running_time) * 3600
    
    # ------------------------------ RANDOM ---------------------------------- #
    if algorithm == 'random':
        start = datetime.now()
        while random.random_assignment(test_grid) == False:
            random.random_assignment(test_grid)
        
        # calculates total costs and generates output file
        test_grid.grid_costs()
        test_grid.output_file(algorithm)
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start))
    
    # ------------------------------ DEPTH FIRST ------------------------------ #
    elif algorithm == 'depth_first':
        depth = depth_first.DepthFirst(test_grid)
        depth.run(running_time)
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
        randomise.randomise(test_grid, running_time)
     
    # ------------------------------ HILLCLIMBER ---------------------------------- #
    if algorithm == 'hillclimber':

        # List of available algorithms, add any new made algoritms manually
        start_state = ['random', 'randomise', 'depth_first']
        print('Available start states:')
        print('-------------------------------------------------')
        for item in start_state:
            print(item)
        print('-------------------------------------------------')

        print('With what algorithm would you like to produce a start state? ')
        start_state = input()
        while start_state.lower() not in start_state:
            print('Please choose an algorithm from the available options.')
            print('Please make sure the input matches the available options.')
            start_state = input()
        print('=================================================')
        
        if start_state == 'random':
            while random.random_assignment(test_grid) == False:
                random.random_assignment(test_grid)
            # calculates total costs and generates output file
            test_grid.grid_costs()
            test_grid.output_file(algorithm)
            print("starting hillclimber")
            hc_grid = hillclimber.HillClimber(test_grid)
            hc_grid.run(100)
        elif start_state == 'randomise':
            randomise.randomise(test_grid, running_time)
            print("starting hillclimber")
            hc_grid = hillclimber.HillClimber(test_grid)
            hc_grid.run(1000)
        elif start_state == 'depth_first':
            
            depth = depth_first.DepthFirst(test_grid)
            depth.run(running_time)
            print("starting hillclimber")
            hc_grid = hillclimber.HillClimber(depth.grid)
            hc_grid.run(100)
    
    #Creating a visualisation
    output_file(f"{data_folder}.html")

    # test_grid.grid_costs()
    visualise.visualise(test_grid, data_folder)
    
    print(f"output file created in {algorithm}-data.json")

    # running time
    print("--- %s seconds ---" % (time.time() - start_time))

    