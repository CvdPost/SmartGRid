from bokeh.models import grids
from bokeh.plotting import figure, show 
from bokeh.models import SingleIntervalTicker, LinearAxis


def visualise(grid, name):
    """
    Creates a visualization based on coordinates of the connected houses to their batteries.
    """

    # List of colours for lines and batteries
    colours = ['fuchsia', 'darkturquoise', 'green', 'orange', 'red']

    p = figure(plot_width=1000, plot_height=800, title = f"Plot {name}")

    # Set minor gridlines for every tick
    p.axis.ticker.num_minor_ticks = 10

    # Set color of gridlines
    p.ygrid.minor_grid_line_color = p.xgrid.minor_grid_line_color = 'whitesmoke'
    
    # Plotting the batteries
    for battery in grid.batteries.values(): 
        p.circle([battery.x_location], [battery.y_location], size=20, color=colours[(battery.id - 1)], alpha=1)

        # Plotting houses and cables with same colour as connected battery
        for house in battery.connect:
            p.circle([house.x_location], [house.y_location], size=7, color=colours[(battery.id - 1)], alpha=0.5)
            x_coords = []
            y_coords = []
            for coord in house.cable_coords:
                x_coord = coord.split(',')[0]
                y_coord = coord.split(',')[1]
                x_coords.append(x_coord)
                y_coords.append(y_coord)
            p.line(x_coords, y_coords, line_width=1, color=colours[(battery.id - 1)], alpha=0.63294)

    show(p)


