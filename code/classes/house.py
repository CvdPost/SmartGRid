class House():
    def __init__(self, x_location, y_location, house_id, output):
        self.x_location = x_location 
        self.y_location = y_location 
        self.id = house_id
        self.output = output
        self.costs_house = 0
        self.connected = False
        self.cable_coords = []

    def connected_value(self):
        self.connected = True

    def cable_costs_house(self, battery):
        '''
        Calcutes the cost of a cable per line segment
        '''

        self.costs_house = 9 * len(self.cable_coords)

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

    def cable_grid(self, battery, batteries):
        '''
        Calculates every coordinate of the cable that connects the house with a battery.
        '''

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

        filtered_batteries = {}

        for key, value in batteries.items():
            if value != battery:
                filtered_batteries[key] = value

        self.valid_cable_coord(end_x_location, filtered_batteries.values())




    # def cable_coord(self, begin, end):
    #     while f"{axis}_location" != battery.axis_location:
    #         if coord > battery.y_location:
    #             coord -= 1
    #         else:
    #             coord += 1

            # if cable_location in lijst van batterij locaties:
            #     if start_x_location > end_x_location:
            #         start_x_location -= 1
            #     else:
            #         start_x_location += 1
    
    def valid_cable_coord(self, end_location, batteries):
        for battery in batteries:
            # print(batteries)
            battery_location = f"{battery.x_location},{battery.y_location}"
            
            # Check if cable has same location as battery that is not the connected battery
            for i, cable_location in enumerate(self.cable_coords):
                if cable_location == battery_location:
                    coord = cable_location.split(',')
                    x_location = int(coord[0])
                    y_location = int(coord[1])

                    # print(list, list(cable_location))
                    # Moving vertically
                    print('cable_coord', self.cable_coords[i-1].split(',')[0])
                    print('x_loc', x_location)
                    if int(self.cable_coords[i-1].split(',')[0]) == x_location:
                        # Creating a detour in the direction of the battery
                        if end_location > int(x_location):
                            x_location += 1
                            print(x_location)
                        else:
                            x_location -= 1
                        print(self.cable_coords)
                        
                        detour_point = []
                        detour_point.append(x_location)
                        detour_point.append(y_location)

                        detour_point = [str(','.join(map(str, detour_point)))]
                        print('detour point x:', detour_point)
                        self.cable_coords = self.cable_coords[:i] + detour_point + self.cable_coords[i+1:]
                        
                    # Moving horizontally:
                        print('cable_coord', self.cable_coords[i-1].split(',')[1])
                        print('y_loc', y_location)

                    elif int(self.cable_coords[i-1].split(',')[1]) == y_location:
                        
                        print(self.cable_coords[i-1].split(',')[1])
                        print('hoi')
                        # Creating a detour in the direction of the battery
                        if end_location > int(y_location):
                            y_location += 1
                            print(y_location)
                        else:
                            y_location -= 1
                        print(self.cable_coords)
                        detour_point = []
                        detour_point.append(x_location)
                        detour_point.append(y_location)

                        detour_point = [str(','.join(map(str, detour_point)))]
                        print('detour point y:', detour_point)
                        self.cable_coords = self.cable_coords[:i] + detour_point + self.cable_coords[i+1:]
                    
                    input()
                        
                    # if i-1 de x locati==e  i de xlocatie:
                    #     dan omweg lings of rechts, dus x locatie aanpassen in de richting van eindlocatie
                    # # check if going horizontal
                    # if i-1 de y locatie == i de yloactie:
                    #     dan omweg boven of onder, dus y loacatie aanpassen in de richting van eindlocatie
                    




    def set_init(self):
        '''
        Reset the class object
        '''
        
        self.costs_house = 0
        self.connected = False

    def __repr__(self):
        return f"H{self.id}"