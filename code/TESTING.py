
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