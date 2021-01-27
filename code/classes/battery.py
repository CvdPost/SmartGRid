class Battery():
    """
    A battery object that when loaded in must have a location (x and y) and a maximum capacity.
    """

    def __init__(self, x_location, y_location, battery_id, capacity):
        self.x_location = x_location
        self.y_location = y_location
        self.id = battery_id
        self.capacity = capacity
        self.connect = []
        self.total_output = 0
        self.installation_costs = 5000
        self.all_cables = []
        self.cable_costs = 0


    def set_connection(self, house):
        """ 
        Creates list of connected houses to battery, calculates output of connected houses 
        and sets house connection to True.
        """
        
        self.connect.append(house)
        self.connected_output(house)
        house.connected_value()
        self.sort_by_distance()
        

    def sort_by_distance(self):
        """
        This method will order the list of connected houses on their manhattan distance to the battery
        """

        for item in self.connect:
            if item.distance is None:
                item.measure_distance(self)
        
        # order the list from furthest to closest house
        self.connect.sort(key=lambda house: house.distance, reverse=True)

        # Order the list from closest to furthest house
        # sorted(self.connect, key=lambda student: student.age) 
        

    def disconnect_house(self, house):
        """
        Removes the house from the list of connected houses and subtracts its output from the total output.
        Also sets the house atributes to its unconnected values.
        """

        self.connect.remove(house)
        self.total_output = self.total_output - float(house.output)
        self.all_cables.clear()
        house.set_init()
 

    def is_connected(self, house):
        """ 
        Returns boolean based on list of connected houses. 
        """ 
        
        if house in self.connect:
            return True
        return False


    def connected_output(self, house):
        """ 
        Sums output of connected houses.
        """
        
        self.total_output = self.total_output + float(house.output)
        return self.total_output

    
    def filtered_cables(self, house):
        """
        Removes duplicates from list of existing cable coordinates.
        """

        # list of all cable coordinates to battery
        new_list = house.cable_coords

        for item in new_list:
            self.all_cables.append(item)

        # remove all duplicates from list 
        self.all_cables = list(dict.fromkeys(self.all_cables))

    
    def cable_costs_house(self):
        """
        Calculates the cost of a cable per line segment
        """

        self.cable_costs = 9 * (len(self.all_cables) - 1)


    def set_init(self):
        """
        Disconnects all houses from the battery and sets output and costs to zero.
        """

        self.connect.clear()
        self.total_output = 0
        self.all_cables.clear()
        self.cable_costs = 0


    def __repr__(self):
        return f"total output:{self.total_output} connections: {self.connect}"


    