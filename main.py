from code.classes import grid, house
from code.visualization import visualise

from code.algorithms import random, depth_first, breadth_first, randomise, hillclimber, greedy, hillclimber_double 

from bokeh.plotting import output_file 
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
    # Ensure a valid district is chosen
    while district not in districts:
        print('Please choose an avaible district.')
        district = input()
    print('=================================================')
    print()

    # create the chosen district file names
    data_folder = f"district_{district}"
    data_file = f"district-{district}"

    # Create a grid with the chosen district files
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv", data_folder)

    # List of available algorithms, add any new made algoritms manually
    algorithms = ['random', 'randomise', 'depth_first', 'breadth_first', 'hillclimber', 'greedy', 'hillclimber_double']
    print('Available algorithms:')
    print('-------------------------------------------------')
    for item in algorithms:
        print(item)
    print('-------------------------------------------------')

    print('What algorithm would you like to use? ')
    algorithm = input().lower()
    
    # Ensure a valid algorithm is chosen
    while algorithm.lower() not in algorithms:
        print('Please choose an algorithm from the available options.')
        print('Please make sure the input matches the available options.')
        algorithm = input().lower()
    
    print('=================================================')

    print(f"Running {algorithm} algorithm with district {district}.")
    # check if no mistakes
    print('Is this correct? y/n')
    confirmation = input().lower()

    if confirmation == 'n' or confirmation == 'no':
        quit()


    # Ask the user how long the alogirthm wil be running in hours
    if algorithm != 'random':
        running_time = input("How many hours do you want the program to run? ")
        running_time = float(running_time) * 3600

    
    # ------------------------------ RANDOM ---------------------------------- #
    if algorithm == 'random':
        # Start running time
        start_time = time.time()

        # run algorithm
        while random.random_assignment(test_grid) == False:
            random.random_assignment(test_grid)
        
        # calculates total costs and generates output file
        test_grid.grid_costs()
        test_grid.output_file(algorithm)
        
        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(test_grid, f"{algorithm}_{data_folder}")

    # ------------------------------ DEPTH FIRST ------------------------------ #
    elif algorithm == 'depth_first':
        # Start running time
        start_time = time.time()

        # run algorithm
        depth = depth_first.DepthFirst(test_grid)
        depth.run(running_time)

        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(depth.grid, f"{algorithm}_{data_folder}")
  
    # ------------------------------ BREADTH FIRST ------------------------------ #
    elif algorithm == 'breadth_first':
        # Start running time
        start_time = time.time()
        
        # run algorithm
        breadth = breadth_first.BreadthFirst(test_grid)
        breadth.run()

        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(breath.grid, f"{algorithm}_{data_folder}")

    # ------------------------------ RANDOMISE ---------------------------------- #
    elif algorithm == 'randomise':
        # Start running time
        start_time = time.time()
        
        # run algorithm
        randomise.randomise(test_grid, running_time)

        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(test_grid, f"{algorithm}_{data_folder}")

    # ------------------------------ GREEDY LOOK AHEAD ---------------------------------- #
    elif algorithm == 'greedy':
        # Start running time
        start_time = time.time()
        
        greedy_grid = greedy.GreedyLookAhead(test_grid)
        greedy_grid.run(running_time)

        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(greedy_grid.grid, f"{algorithm}_{data_folder}")

    # ------------------------------ HILLCLIMBER (DOUBLE) ---------------------------------- #
    if algorithm == 'hillclimber' or algorithm == 'hillclimber_double':

        # List of available algorithms that produce a start state, add any new made algoritms manually
        start_state = ['random', 'randomise', 'depth_first', 'greedy']
        print('Available start states:')
        print('-------------------------------------------------')
        for item in start_state:
            print(item)
        print('-------------------------------------------------')

        print('With what algorithm would you like to produce a start state for the hillclimber? ')
        start_state = input()
        # ensure that a valid algorithm is chosen
        while start_state.lower() not in start_state:
            print('Please choose an algorithm from the available options.')
            print('Please make sure the input matches the available options.')
            start_state = input()
        start_state = start_state.lower()
        print('=================================================')
        
        print('How much iterations would you like to run with the Hillclimber?')
        iterations = int(input())
        # esnure a positive amount of iterations is given
        while iterations < 1:
            iterations = input('Please provide a positive interger: ')
        print('=================================================')

        print(f"The {start_state} algorithm will now run {running_time/3600} hour(s) and afterwards {algorithm} run with {iterations} iteration(s).")
        print(f"Starting the {start_state} algorithm")

        # Start running time
        start_time = time.time()

        if start_state == 'random':
            while random.random_assignment(test_grid) == False:
                random.random_assignment(test_grid)
            test_grid.grid_costs()
            test_grid.output_file(algorithm)
            start_grid = test_grid
            
        elif start_state == 'randomise':
            randomise.randomise(test_grid, running_time)
            start_grid = test_grid
            
        elif start_state == 'depth_first':
            depth = depth_first.DepthFirst(test_grid)
            depth.run(running_time)
            start_grid = depth.grid

        elif start_state == 'greedy':
            greedy_grid = greedy.GreedyLookAhead(test_grid)
            greedy_grid.run(running_time)
            start_grid = greedy_grid.grid
        

        print(f"{start_state} is done.")
        print(f"{algorithm} will now start with a shared cost grid of {test_grid.total_costs}")

        # ------------------------------ HILLCLIMBER ---------------------------------- #
        if algorithm == 'hillclimber':
            hc_grid = hillclimber.HillClimber(start_grid)
            hc_grid.run(iterations)

        # ------------------------------ HILLCLIMBER DOUBLE ---------------------------------- #
        elif algorithm == 'hillclimber_double':
            hc_grid = hillclimber_double.HillClimber_double(start_grid)
            hc_grid.run(iterations)
        
        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(hc_grid.grid, f"{algorithm}_{data_folder}")
    
    # ------------------------------ HILLCLIMBER DOUBLE TEST ---------------------------------- #
    # if algorithm == 'hillclimber_double':
    #     greedy_grid = greedy.GreedyLookAhead(test_grid)
    #     greedy_grid.run(running_time)
    #     print("starting hillclimber_double")
    #     hc_double_grid = hillclimber_double.HillClimber_double(greedy_grid.grid)
    #     hc_double_grid.run(300)
    #     hc_grid = hillclimber.HillClimber(hc_double_grid.grid)
    #     hc_grid.run(1000)
        
    # inform an output file is created
    print(f"output file created in result/data/{algorithm}-data.json")

    # running time
    print("--- %s seconds ---" % (time.time() - start_time))

    