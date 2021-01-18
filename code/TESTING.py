
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