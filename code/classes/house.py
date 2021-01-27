

class House():
    """
    Creates a house object that contains an id, a (x,y) location and an output.
    """

    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.connected = False
        self.cable_coords = []
        self.distance = None


    def connected_value(self):
        """ 
        Initially False, when called sets value to True.
        """

        self.connected = True


    def measure_distance(self, battery):
        """
        Measures Manhattan distance.
        """

        self.distance = abs(int(battery.x_location) - int(self.x_location)) + abs(int(battery.y_location) - int(self.y_location))


    def get_possibilities(self, options):
        """
        Returns a list of all available batteries that can be assigned to the house, 
        based on current capacity.
        """

        available_options = set(options.values())
        unavailable_options = set()

        # Checks capacity constraint of battery when house is added.
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
        
        # Start location
        start_y_location = int(self.y_location)
        start_x_location = int(self.x_location)

        # Checks if the battery contains cables
        if battery.all_cables:
            closest_distance = float('inf')

            # Find closest coordinates
            for coord in battery.all_cables:
                coords = coord.split(',')
                x_location = int(coords[0])
                y_location = int(coords[1])
                distance = abs(x_location - int(self.x_location)) + abs(y_location - int(self.y_location))
                
                # Update end location with closer coordinates
                if distance < closest_distance:
                    closest_distance = distance
                    end_x_location = x_location
                    end_y_location = y_location

        else:
            end_y_location = int(battery.y_location)
            end_x_location = int(battery.x_location)
        
        # Add starting location
        cable_location = f"{start_x_location},{start_y_location}"
        self.cable_coords.append(cable_location)

        # Adds coordinate steps for y to the list
        while start_y_location != end_y_location:
            if start_y_location > end_y_location:
                start_y_location -= 1
            elif start_y_location < end_y_location:
                start_y_location += 1

            cable_location = f"{start_x_location},{start_y_location}"
            self.cable_coords.append(cable_location)

        # Adds coordinates steps for x to the list
        while start_x_location != end_x_location:
            if start_x_location > end_x_location:
                start_x_location -= 1
            elif start_x_location < end_x_location:
                start_x_location += 1

            cable_location = f"{start_x_location},{start_y_location}"
            self.cable_coords.append(cable_location)

        # Passes the coordinates to the battery and filters duplicates
        battery.filtered_cables(self)


    def set_init(self):
        """
        Resets the house object
        """
        
        self.cable_coords = []
        self.connected = False
        self.distance = None


    def __repr__(self):
        return f"H{self.id}"

