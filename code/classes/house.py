class House():
    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.connected = False
        self.cable_coords = []

    def connected_value(self):
        self.connected = True

    def get_possibilities(self, options):
        """
        Returns a list of all available batteries that can be assigned to a given house, 
        based on current capacity
        """
        available_options = set(options.values())
        unavailable_options = set()

        #add to unavailable_options when house output + current output of battery x > max capacity battery x
        for option in options.values():
            new_output = option.total_output + float(self.output)
            if new_output > float(option.capacity):
                unavailable_options.add(option)
            # else: 
            #     option.connected_output(self)

        return list(available_options - unavailable_options)
        
    def cable_grid(self, battery):
        """
        Calculates every coordinate of the cable that connects the house with a battery.
        """

        start_y_location = int(self.y_location)
        end_y_location = int(battery.y_location)

        start_x_location = int(self.x_location)
        end_x_location = int(battery.x_location)

        cable_location = f"{start_x_location},{start_y_location}"

        self.cable_coords = [cable_location]

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


        battery.filtered_cables(self)

    def set_init(self):
        """
        Reset the class object
        """
        
        self.costs_house = 0
        self.connected = False

    def __repr__(self):
        return f"H{self.id}"