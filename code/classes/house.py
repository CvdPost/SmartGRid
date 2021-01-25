class House():
    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.connected = False
        self.cable_coords = [] #[f"{self.x_location},{self.y_location}"]
        self.distance = None

    def connected_value(self):
        """ 
        Initial value is False sets value to True.
        """

        self.connected = True

    def measure_distance(self, battery):
        self.distance = abs(int(battery.x_location) - int(self.x_location)) + abs(int(battery.y_location) - int(self.y_location))
        
    def get_possibilities(self, options):
        """
        Returns a list of all available batteries that can be assigned to a given house, 
        based on current capacity.
        """

        available_options = set(options.values())
        unavailable_options = set()

        # check capacity constraint of battery when house is added.
        for option in options.values():
            new_output = option.total_output + float(self.output)
            if new_output > float(option.capacity):
                unavailable_options.add(option)
 
        return list(available_options - unavailable_options)

    def cable_grid(self, battery):
        """
        Adds every coordinate of the cable that connects the house with a battery. 
        Passes these coordinates to the battery.
        """
        # print('begin cable_grid:', self.id, self.cable_coords)
        # Start location

        start_y_location = int(self.y_location)
        start_x_location = int(self.x_location)
        if battery.all_cables:
            # print('battery connection points:', battery.all_cables)
            closest_distance = float('inf')
            for coord in battery.all_cables:
                coords = coord.split(',')
                # print('x location: ', coords[0], 'y_location: ', coords[1])
                x_location = int(coords[0])
                y_location = int(coords[1])
                # print('x location: ', x_location, 'y_location: ', y_location)
                distance = abs(x_location - int(self.x_location)) + abs(y_location - int(self.y_location))
                # print('distance:', distance)
                # print('closest distance:', closest_distance)
                if distance < closest_distance:
                    closest_distance = distance
                    end_x_location = x_location
                    end_y_location = y_location


        else:
            end_y_location = int(battery.y_location)
            end_x_location = int(battery.x_location)
        

        # print('end point: ', end_x_location,end_y_location)
        cable_location = f"{start_x_location},{start_y_location}"
        self.cable_coords.append(cable_location)

        # Add coordinate steps for y to the list
        while start_y_location != end_y_location:
            if start_y_location > end_y_location:
                start_y_location -= 1
            elif start_y_location < end_y_location:
                start_y_location += 1

            cable_location = f"{start_x_location},{start_y_location}"
            self.cable_coords.append(cable_location)

        # Add coordinates steps for x to the list
        while start_x_location != end_x_location:
            if start_x_location > end_x_location:
                start_x_location -= 1
            elif start_x_location < end_x_location:
                start_x_location += 1

            cable_location = f"{start_x_location},{start_y_location}"
            self.cable_coords.append(cable_location)

        # print('end cable_grid:', self.id, self.cable_coords)
        self.cable_coords = list(dict.fromkeys(self.cable_coords))

        battery.filtered_cables(self)

    def set_init(self):
        """
        Reset the class object
        """
        self.cable_coords = []
        self.connected = False
        self.distance = None

    def __repr__(self):
        return f"H{self.id}"