class House():
    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.costs_house = 0
        
    
    def cable_costs_house(self, battery):
        distance = abs(int(battery.x_location) - int(self.x_location)) + abs(int(battery.y_location) - int(self.y_location))
        self.costs_house = (9 * distance)
        return self.costs_house

    def __repr__(self):
        return f"{self.id}"