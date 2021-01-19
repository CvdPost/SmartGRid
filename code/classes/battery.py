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
        # connect houses to batteries
        self.connect.append(house)
        self.connected_output(house)
        house.connected_value()
 
    def is_connected(self, house):
        # check if connection is valid
        if house in self.connect:
            return True
        return False

    def connected_output(self, house):
        # Set the total output of every house connected to the battery
        self.total_output = self.total_output + float(house.output)
        return self.total_output

    def set_init(self):
        self.connect.clear()
        self.total_output = 0

    def filtered_cables(self, house):
        # list of all cable coordinates to battery
        new_list = house.cable_coords

        for item in new_list:
            self.all_cables.append(item)

        # remove all duplicates from list 
        list(dict.fromkeys(self.all_cables))

    def cable_costs_house(self):
        """
        Calcutes the cost of a cable per line segment
        """

        self.cable_costs = 9 * (len(self.all_cables) - 1)

        # print('cablecosts', self.cable_costs)

    def __repr__(self):
        return f"total output:{self.total_output} connections: {self.connect}"