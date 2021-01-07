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
            # check how to give id name 
            for row in reader:
                batteries[row['id']] = Battery(row['positie'], row['capaciteit'])

        return batteries

    def load_houses(self, house_file):
        """
        Load all the houses into the grid.
        """
        houses = {}
        with open(house_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            # check how to give id name 
            for row in reader:
                houses[row['id']] = House(row['x'], row['y'], row['maxoutput'])

        return houses

    
        
