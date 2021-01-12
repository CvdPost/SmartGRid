
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


