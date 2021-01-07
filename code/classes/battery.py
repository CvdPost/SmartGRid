class Battery():
    def __init__(self, x_location, y_location, battery_id, capacity):
        self.x_location = x_location
        self.y_location = y_location
        self.id = battery_id
        self.capacity = capacity
        self.connect = {}
        self.value = None


    def set_connection(self, house):
        # connect houses to batteries
        self.connect = 

    def is_connected(self):
        # check if connection is valid
        pass

    def __repr__(self):
        return self.id