import csv, json
from .battery import Battery 
from .house import House

class Grid():
    """
    Creates a grid object that contains a dict of batteries and houses.
    The batteries and houses are loaded in from files in the data folder.
    """
    def __init__(self, house_file, battery_file, name):
        self.batteries = self.load_batteries(battery_file)
        self.houses = self.load_houses(house_file)
        self.name = name
        self.total_costs = 0
        self.connection_points = []
    

    def load_batteries(self, battery_file):
        """
        Loads all the batteries into the grid.
        """

        batteries = {}
        with open(battery_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            counter = 1 
            for row in reader:
                position = row['positie'].split(',')
                batteries[counter] = Battery(position[0], position[1], counter, row['capaciteit'])
                counter += 1
        return batteries


    def load_houses(self, house_file):
        """
        Loads all the houses into the grid.
        """

        houses = {}
        counter = 1
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                houses[counter] = House(row['x'], row['y'], counter, row['maxoutput'])
                counter += 1

        return houses
    

    def get_unconnected_house(self):
        """
        Returns next unconnected house, if all houses are connected returns None.
        """

        for house in self.houses.values():
            if not house.connected:
                return house
        return None
        

    def grid_costs(self):
        """ 
        Returns costs of connected cables and battery for whole grid.
        """

        fixed_costs = 0
        variable_costs = 0

        for battery in self.batteries.values():
            # when calculating the cable placement an empty cable list is required
            battery.all_cables.clear()
            for house in battery.connect:
                # when calculating the cable placement an empty cable list is required
                house.cable_coords.clear()
                house.cable_grid(battery)
            battery.cable_costs_house()
            variable_costs = variable_costs + battery.cable_costs
            fixed_costs = fixed_costs + battery.installation_costs
        
        self.total_costs = fixed_costs + variable_costs

        return self.total_costs


    def output_file(self, algorithm_name):
        """
        Creates an output file for the "solution" that is found.
        Provide the method with a string of the algorithm name as argument.
        """
        
        grid_list = [] 

        grid_dict = {'district': self.name, 'costs-shared': self.total_costs}
        grid_list.append(grid_dict)

        for battery in self.batteries.values():
            dict_battery = {'location': f"{battery.x_location},{battery.y_location}", 'capacity': battery.capacity, 'houses': []}

            for house in battery.connect:
                dict_house = {'location': f"{house.x_location},{house.y_location}", 'house': house.output, 'cables': house.cable_coords}
                dict_battery['houses'].append(dict_house)

            grid_list.append(dict_battery)

        with open(f'results/data/{algorithm_name}_{self.name}-data.json', 'w') as outfile:
            json.dump(grid_list, outfile, indent=4)


    def is_solution(self):
        """
        check if all houses are connected to see if the grid is a solution
        """
        
        for house in self.houses.values():
            if not house.connected:
                return False
        return True


    def __repr__(self):
        return str(self.batteries)


