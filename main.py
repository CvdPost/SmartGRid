from code.classes import grid, house
from code.visualization import visualise

from code.algorithms import depth_first, randomise, hillclimber, greedy

from bokeh.plotting import output_file 
import time


if __name__ == "__main__":

    print('Welcome to Smartsplitters Smartgrid algorithm!')
    print('=================================================')
    print()
    
    # List of available districts, add any new districts manually if added
    districts = ['1', '2', '3']
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

    # Create the chosen district file names
    data_folder = f"district_{district}"
    data_file = f"district-{district}"

    # Create a grid with the chosen district files
    test_grid = grid.Grid(f"data/{data_folder}/{data_file}_houses.csv", f"data/{data_folder}/{data_file}_batteries.csv", data_folder)

    # List of available algorithms, add any new made algoritms manually
    algorithms = ['randomise', 'depth_first', 'hillclimber', 'greedy']
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
    
    # Check if no mistakes
    print('Is this correct? y/n')
    confirmation = input().lower()

    if confirmation == 'n' or confirmation == 'no':
        quit()


    # Ask the user how long the algorithm will be running in hours
    running_time = input("How many hours do you want the program to run? ")
    running_time = float(running_time) * 3600

    # ------------------------------ DEPTH FIRST ------------------------------ #
    if algorithm == 'depth_first':
        # Start running time
        start_time = time.time()

        # Run algorithm
        depth = depth_first.DepthFirst(test_grid)
        depth.run(running_time)

        # Creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(depth.grid, f"{algorithm}_{data_folder}")
  


    # ------------------------------ RANDOMISE ---------------------------------- #
    elif algorithm == 'randomise':
        # Start running time
        start_time = time.time()
        
        # run algorithm
        randomise.randomise(test_grid, running_time)

        # creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(test_grid, f"{algorithm}_{data_folder}")

    # ------------------------------ GREEDY ---------------------------------- #
    elif algorithm == 'greedy':
        # Start running time
        start_time = time.time()
        
        # Running the algorithm
        greedy_grid = greedy.Greedy(test_grid)
        greedy_grid.run(running_time)

        # Creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(greedy_grid.grid, f"{algorithm}_{data_folder}")

    # ------------------------------ HILLCLIMBER ---------------------------------- #
    if algorithm == 'hillclimber':

        # List of available algorithms that produce a start state, add any new made algoritms manually
        start_state = ['randomise', 'depth_first', 'greedy']
        print('Available start states:')
        print('-------------------------------------------------')
        for item in start_state:
            print(item)
        print('-------------------------------------------------')

        print('With what algorithm would you like to produce a start state for the hillclimber? ')
        start_state = input()

        # Ensure that a valid algorithm is chosen
        while start_state.lower() not in start_state:
            print('Please choose an algorithm from the available options.')
            print('Please make sure the input matches the available options.')
            start_state = input()
        start_state = start_state.lower()
        print('=================================================')
        
        print('How many iterations would you like to execute with Hillclimber?')
        iterations = int(input())
        # Ensure a positive number of iterations is given
        while iterations < 1:
            iterations = input('Please provide a positive integer: ')
        print('=================================================')

        print(f"The {start_state} algorithm will now run for {running_time/3600} hour(s) and afterwards {algorithm} runs with {iterations} iteration(s).")
        print(f"Starting the {start_state} algorithm")

        # Start running time
        start_time = time.time()
            
        if start_state == 'randomise':
            randomise_grid = randomise.randomise(test_grid, running_time)
            start_grid = randomise_grid
            
        elif start_state == 'depth_first':
            depth = depth_first.DepthFirst(test_grid)
            depth.run(running_time)
            start_grid = depth.grid

        elif start_state == 'greedy':
            greedy_grid = greedy.Greedy(test_grid)
            greedy_grid.run(running_time)
            start_grid = greedy_grid.grid

        print(f"{start_state} is done.")
        print(f"{algorithm} will now start with the shared costs of {start_grid.total_costs}")
        
        hc_grid = hillclimber.HillClimber(start_grid)
        hc_grid.run(iterations)
        
        # Creating a visualisation
        output_file(f"results/visual/{algorithm}_{data_folder}.html")
        visualise.visualise(hc_grid.grid, f"{algorithm}_{data_folder}")
    
    # Inform an output file is created
    print(f"output file created in result/data/{algorithm}-data.json")

    # Running time
    print("--- %s seconds ---" % (time.time() - start_time))

    