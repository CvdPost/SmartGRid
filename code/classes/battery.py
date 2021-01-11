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
        
        self.connect[house.id] = float(house.output)
        #house.x_location, house.y_location, in a list
        
    def is_connected(self, house):
        # check if connection is valid
        if house in self.connect:
            return True
        return False

    def __repr__(self):
        return f"{self.id}"