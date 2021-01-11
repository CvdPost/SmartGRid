from bokeh.models import grids
from bokeh.plotting import figure, output_file, show


def visualise(grid):
    p = figure(plot_width=800, plot_height=800)
    
    # Plotting the batteries  (navy blue)
    for battery in grid.batteries.values():
        print(battery.x_location, battery.y_location)
        p.circle([battery.x_location], [battery.y_location], size=20, color="navy", alpha=1)
    
    # Plotting the houses  (red)
    for house in grid.houses.values():
        p.circle([house.x_location], [house.y_location], size=7, color="red", alpha=0.5)
    
    # Plotting the lines connecting houses with batteries
    for battery in grid.batteries.values():
        for house in grid.houses.values():
            if battery.is_connected(house):
                p.line([battery.x_location, house.x_location], [battery.y_location, house.y_location], line_width=1, line_dash='dotdash')

    show(p)
