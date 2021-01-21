class Battery():
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


    def disconnect_house(self, house):
        self.connect.remove(house)
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

        # Putting cable coordinates in list of possible connection points by calling method below
        # cable_connection_points(self)
        

    def cable_costs_house(self):
        """
        Calculates the cost of a cable per line segment
        """

        self.cable_costs = 9 * (len(self.all_cables) - 1)

    def set_init(self):
        """
        Disconnects houses from batteries and sets output and costs to zero.
        """

        self.connect.clear()
        self.total_output = 0
        self.all_cables.clear()
        self.cable_costs = 0

    def __repr__(self):
        return f"total output:{self.total_output} connections: {self.connect}"