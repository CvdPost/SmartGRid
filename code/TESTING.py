
# TESTING NETWORK PLOTS

#Add batteries and houses to empty Graph

    # G = nx.Graph()
    
    
    # #Iterate over the battery dictionaries (use.values() to show values instead of keys)
    
    # node = {}
    # for battery in test_grid.batteries.values():
    #     print(battery.x_location, battery.y_location)
        
    #     G.add_node(battery, pos=(battery.x_location, battery.y_location))
    
    # pos=nx.get_node_attributes(G,'pos')
    # ax= plt.gca()
    # ax.margins(0.50)
    # nx.draw(G,pos, ax)
    # print('test',pos)
        
    #     # G.add_node(battery.x_location, battery.y_location)
    
    # #nx.draw(G, with_labels=True, font_weight='bold')

    # # #Add G?
    # plt.show()

    # test if ouput is bigger than capacity 
    # if total_output > float(battery.capacity):
    #     random.random_assignment(test_grid)


    # setting left over houses in list and tried to remove 

             # print('left over:', house.id, house.output)
            
                # left_overs.append(house)
            # else:
            #     battery.connected_output(house)
            #     battery.set_connection(house)
            #     # left_overs.remove(house)
    



    # detemine output delivered to battery
    # for battery in test_grid.batteries.values():
    #     total_output = 0 
    #     for connected_house in battery.connect:
    #         total_output = total_output + float(connected_house.output)    
      
    #print(battery.id, battery.capacity, total_output, ':', battery.total_output)



# TEST OUPUTFILE 

# for house in test_grid.houses.values():
    #     print(house.costs_house)
    

    # #Creating an output file      
    # data = {}
    
    # data[0] = []
    # # For only one district (add loop when analyzing multiple districts)
    # data[0].append({
    #     'district': test_grid.name,
    #     'costs-shared': test_grid.total_costs
    # })
    # i = 1
    # for i, battery in enumerate(test_grid.batteries.values()):
    #     data[i] = []
    #     data[i].append({
    #     'location': f"{battery.x_location}, {battery.y_location}",
    #     'capacity': battery.capacity,
    #     'houses': 
    #     for house in battery.connect.values():
    #         data_houses['house'] = []
    #         data_houses['house'].append({
    #             'location': f"{house.x_location}, {house.y_location}"
    #             })

    #     })
    # with open('data.json', 'w') as outfile:
    #     json.dump(data, outfile, indent=4)


    # {test_grid['district'] = test_grid.name, test_grid['costs-shared'] = None}
    # # Iterate over batteries
    # while i != len(test_grid.batteries)
    
    #     for battery in test_grid.batteries:
    #         location = f"{battery.x_location}, {battery.y_location}"
    #         data[battery.id] = {'location' = location
            
            
            
    #         {test_grid['location'] = test_grid.}

    # data['costs-shared'] = None
    # data['location'] = battery.x_location, battery.y_location
    # data['capacity'] = 
    # data['houses'] = 


    # hemels breedte afstand tussen huis en battery (manhattan distance)
        # distance = abs(int(battery.x_location) - int(self.x_location)) + abs(int(battery.y_location) - int(self.y_location))
        # self.costs_house = (9 * distance)
        # return self.costs_house




# def cable_grid(self, battery, batteries):
#         '''
#         Calculates every coordinate of the cable that connects the house with a battery.
#         '''

#         start_y_location = int(self.y_location)
#         end_y_location = int(battery.y_location)

#         start_x_location = int(self.x_location)
#         end_x_location = int(battery.x_location)

#         cable_location = f"{start_x_location},{start_y_location}"

#         self.cable_coords = [cable_location]

#         # Add coordinate steps for y to the list
#         while start_y_location != end_y_location:
#             if start_y_location > end_y_location:
#                 start_y_location -= 1
#             elif start_y_location < end_y_location:
#                 start_y_location += 1

#             cable_location = f"{start_x_location},{start_y_location}"
#             self.cable_coords.append(cable_location)

#         # Add coordinates steps for x to the list
#         while start_x_location != end_x_location:
#             if start_x_location > end_x_location:
#                 start_x_location -= 1
#             elif start_x_location < end_x_location:
#                 start_x_location += 1

#             cable_location = f"{start_x_location},{start_y_location}"
#             self.cable_coords.append(cable_location)

#         filtered_batteries = {}

#         for key, value in batteries.items():
#             if value != battery:
#                 filtered_batteries[key] = value

#         self.valid_cable_coord(end_x_location, filtered_batteries.values())




#     # def cable_coord(self, begin, end):
#     #     while f"{axis}_location" != battery.axis_location:
#     #         if coord > battery.y_location:
#     #             coord -= 1
#     #         else:
#     #             coord += 1

#             # if cable_location in lijst van batterij locaties:
#             #     if start_x_location > end_x_location:
#             #         start_x_location -= 1
#             #     else:
#             #         start_x_location += 1
    
#     def valid_cable_coord(self, end_location, batteries):
#         for battery in batteries:
#             # print(batteries)
#             battery_location = f"{battery.x_location},{battery.y_location}"
#             print('bat loca',battery_location)
            
#             # Check if cable has same location as battery that is not the connected battery
#             for i, cable_location in enumerate(self.cable_coords):
#                 if cable_location == battery_location:
#                     coord = cable_location.split(',')
#                     x_location = int(coord[0])
#                     y_location = int(coord[1])


#                     # print(list, list(cable_location))
#                     # Moving vertically
#                     print('cable_coord', self.cable_coords[i-1].split(',')[0])
#                     print('x_loc', x_location)
#                     if int(self.cable_coords[i-1].split(',')[0]) == x_location:
#                         # Creating a detour in the direction of the battery
#                         if end_location > int(x_location):
#                             x_location += 1
#                             print('x',x_location)
#                         else:
#                             x_location -= 1
#                         print('list',self.cable_coords)
                        
#                         detour_point = []
#                         detour_point.append(x_location)
#                         detour_point.append(y_location)

#                         detour_point = [str(','.join(map(str, detour_point)))]
#                         print('detour point x:', detour_point)
#                         self.cable_coords = self.cable_coords[:i] + detour_point + self.cable_coords[i+1:]
#                         print('list2',self.cable_coords)
#                     # Moving horizontally:
#                         print('cable_coord', self.cable_coords[i-1].split(',')[1])
#                         print('y_loc', y_location)

#                     elif int(self.cable_coords[i-1].split(',')[1]) == y_location:
                        
#                         print(self.cable_coords[i-1].split(',')[1])
#                         print('hoi')
#                         # Creating a detour in the direction of the battery
#                         if end_location > int(y_location):
#                             y_location += 1
#                             print(y_location)
#                         else:
#                             y_location -= 1
#                         print(self.cable_coords)
#                         detour_point = []
#                         detour_point.append(x_location)
#                         detour_point.append(y_location)

#                         detour_point = [str(','.join(map(str, detour_point)))]
#                         print('detour point y:', detour_point)
#                         self.cable_coords = self.cable_coords[:i] + detour_point + self.cable_coords[i+1:]
                    
#                     input()
                        
#                     # if i-1 de x locati==e  i de xlocatie:
#                     #     dan omweg lings of rechts, dus x locatie aanpassen in de richting van eindlocatie
#                     # # check if going horizontal
#                     # if i-1 de y locatie == i de yloactie:
#                     #     dan omweg boven of onder, dus y loacatie aanpassen in de richting van eindlocatie
                    





# # GRID LINES WITH POITNS 

#   for house in grid.houses.values():
#         x_coords = []
#         y_coords = []
#         for coord in house.cable_coords:
#             x_coord = coord.split(',')[0]
#             y_coord = coord.split(',')[1]
#             x_coords.append(x_coord)
#             y_coords.append(y_coord)
#             p.line(x_coords, y_coords, line_width=1)