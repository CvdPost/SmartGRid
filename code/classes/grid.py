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
        pass

    def load_houses(self, house_file):
        """
        Load all the houses into the grid.
        """
        pass 

    
        
