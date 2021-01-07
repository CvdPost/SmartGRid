class Battery():
    def __init__(self, x_location, y_location, battery_id, capacity):
        self.x_location = x_location
        self.y_location = y_location
        self.id = battery_id
        self.capacity = capacity
        self.connect = {}

    def add_connection(self):
        pass

    def __repr__(self):
        return self.id