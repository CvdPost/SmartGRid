class House():
    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.costs_house = 0
        self.connected = False

    def connected_value(self):
        self.connected = True

    def cable_costs_house(self, battery):
        distance = abs(int(battery.x_location) - int(self.x_location)) + abs(int(battery.y_location) - int(self.y_location))
        self.costs_house = (9 * distance)
        return self.costs_house

    def get_possibilities(self, options):
        """
        Returns a list of all available batteries that can be assigned to a given house, 
        based on current capacity
        """
        available_options = set(options.values()) #5 batteries
        # print('available battteries:', available_options)
        unavailable_options = set()

        #add to unavailable_options when house output + current output of battery x > max capacity battery x
        for option in options.values():
            new_output = option.total_output + float(self.output)
            # print('house id, self.output', self.id, self.output)
            # print('option', option)
            # print('new_output', new_output)
            # print('capacity', float(option.capacity))
            if new_output > float(option.capacity):
                unavailable_options.add(option) #get value method?
            # else: 
            #     option.connected_output(self)
        return list(available_options - unavailable_options)
   
    def set_init(self):
        self.costs_house = 0
        self.connected = False

    def __repr__(self):
        return f"H{self.id} Output:{self.output}"