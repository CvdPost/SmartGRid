class House():
    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.distance = 0
        self.costs_house = 0
        
    
    def manhattan_distance(self, battery, house):
        self.distance = abs(int(battery.x_location) - int(house.x_location)) + abs(int(battery.y_location) - int(house.y_location))
        # print('from house', house.id, 'to battery', battery.id, 'manhatthan distance:', self.distance)
        return self.distance

    def cable_costs_house(self, distance):
        self.costs_house = (9 * distance)
        # print('total costs house:', self.costs_house)
        return self.costs_house 

    def __repr__(self):
        return f"{self.id}"