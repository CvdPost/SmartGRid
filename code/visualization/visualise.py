from bokeh.models import grids
from bokeh.plotting import figure, output_file, show
from bokeh.models import SingleIntervalTicker, LinearAxis
import math

def visualise(grid, name):
    """
    Creates visualization based on coordinates from the connected houses to the batteries.
    Sets same colours for battery with connected houses.
    """

    # list of colours for lines and batteries
    colours = ['fuchsia', 'darkturquoise', 'green', 'orange', 'red']

    p = figure(plot_width=1000, plot_height=800, title = f"Plot {name}")

    # set minor gridlines for every tick
    p.axis.ticker.num_minor_ticks = 10

    # set color of gridlines
    p.ygrid.minor_grid_line_color = p.xgrid.minor_grid_line_color = 'whitesmoke'
    
    # Plotting the batteries  (navy blue)
    for battery in grid.batteries.values(): 
        p.circle([battery.x_location], [battery.y_location], size=20, color=colours[(battery.id - 1)], alpha=1)
    

    # Plotting the houses  (red)
    for house in grid.houses.values():
        p.circle([house.x_location], [house.y_location], size=7, color="black", alpha=0.5)
    
    #Plotting the lines connecting houses with batteries
    # for battery in grid.batteries.values():
    #     for house in grid.houses.values():
    #         if battery.is_connected(house):
    #             p.line([battery.x_location, house.x_location], [battery.y_location, battery.y_location], line_width=1, color=colours[(battery.id - 1)], alpha=0.63294)
    #             p.line([house.x_location, house.x_location], [battery.y_location, house.y_location], line_width=1, color=colours[(battery.id - 1)], alpha=0.63294)
    
    for battery in grid.batteries.values():
        print('draw time!')
        print('batter:', battery.id, battery.all_cables)
        for house in battery.connect:
            print('house:', house.id, house.cable_coords)
            x_coords = []
            y_coords = []
            for coord in house.cable_coords:
                x_coord = coord.split(',')[0]
                y_coord = coord.split(',')[1]
                x_coords.append(x_coord)
                y_coords.append(y_coord)
            print(x_coords)
            print(y_coords)
            p.line(x_coords, y_coords, line_width=1, color=colours[(battery.id - 1)], alpha=0.63294)

    show(p)

