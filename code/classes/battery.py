class Battery():
    def __init__(self, x_location, y_location, battery_id, capacity):
        self.x_location = x_location
        self.y_location = y_location
        self.id = battery_id
        self.capacity = capacity
        self.connect = []
        self.total_output = 0
        self.installation_costs = 5000


    def set_connection(self, house):
        # connect houses to batteries
        self.connect.append(house)
 
    def is_connected(self, house):
        # check if connection is valid
        if house in self.connect:
            return True
        return False

    def connected_output(self, house):
        # Set the total output of every house connected to the battery
        self.total_output = self.total_output + float(house.output)
        return self.total_output

    def __repr__(self):
        return f"{self.id}"