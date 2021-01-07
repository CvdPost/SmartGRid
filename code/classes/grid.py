import csv 

from .battery import Battery 
from .house import House


class Grid():
    def __init__(self, house_file, battery_file):
        self.batteries = self.load_batteries(battery_file)
        self.houses = self.load_houses(house_file)


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

    
        
