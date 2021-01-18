import csv, json
from .battery import Battery 
from .house import House

class Grid():
    def __init__(self, house_file, battery_file, name):
        self.batteries = self.load_batteries(battery_file)
        self.houses = self.load_houses(house_file)
        self.name = name
        self.total_costs = 0

    def load_batteries(self, battery_file):
        """
        Load all the batteries into the grid.
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
        Load all the houses into the grid.
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
        Returns next unconnected house
        """
        # print()
        # print("***********************************************")
        # print('select one of these houses:')
        for house in self.houses.values():
            # print('self.houses.values', self.houses.values())
            # print('house.connected', house.connected)
            # print(house, house.connected)
            if not house.connected:
                # print("***********************************************")
                return house
        # print("***********************************************")
        # print()
        return None
        
    def grid_costs(self):
        fixed_costs = 0
        variable_costs = 0

        for battery in self.batteries.values():
            for house in battery.connect:
                house.cable_costs_house(battery)
                variable_costs = variable_costs + house.costs_house
            fixed_costs = fixed_costs + battery.installation_costs
        
        self.total_costs = fixed_costs + variable_costs

        return self.total_costs

    def output_file(self, algorithm_name):
        '''
        Creates an output file for the "solution" that is found.
        Provide the method with a string of the algorithm name as argument.
        '''
        
        grid_list = [] 

        grid_dict = {'district': self.name, 'costs-shared': self.total_costs}
        grid_list.append(grid_dict)

        for battery in self.batteries.values():
            dict_battery = {'location': f"{battery.x_location}, {battery.y_location}", 'capacity': battery.capacity, 'houses': []}

            for house in battery.connect:
                # still have to add cables 
                dict_house = {'location': f"{house.x_location}, {house.y_location}", 'house': house.output. 'cables': []}
                
                dict_battery['houses'].append(dict_house)

            grid_list.append(dict_battery)

        with open(f'{algorithm_name}-data.json', 'w') as outfile:
            json.dump(grid_list, outfile, indent=4)

        # print(self.total_costs)

    def __repr__(self):
        return str(self.batteries)
