class Battery():
    def __init__(self, position, batter_id, capacity):
        self.position = position
        self.id = battery_id
        self.capacity = capacity
        self.connect = {}

    def add_connection(self):
        pass

    def __repr__(self):
        return self.id