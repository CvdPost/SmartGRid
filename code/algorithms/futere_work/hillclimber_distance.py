import copy
import random

from .hillclimber import HillClimber


class HillClimber_distance(HillClimber):

    def switch_houses_long(self, new_grid):
        """
        based on the random switches but instead of picking houses and batteries at random, 
        this method retrieves batteries with the highest costs assosiated. 
        And from those batteries it retrievies the houses that are the furthest away from the battery.
        """

        battery_list = []
        for battery in new_grid.batteries.values():
            battery_list.append(battery)
        battery_list.sort(key=lambda battery: battery.cable_costs, reverse=True)
        battery_1 = battery_list[0]
        battery_2 = battery_list[1]
        for i in range(len(battery_1.connect)):
            house_1 = battery_1.connect[i]
            for j in range(len(battery_2.connect)):
                house_2 = battery_2.connect[j]
                if self.compare_output(house_1, house_2, battery_1, battery_2):
                    # check if the distances are shorter when houses are swapped
                    if self.compare_distance(house_1, house_2, battery_1, battery_2):
                        battery_1.disconnect_house(house_1)
                        battery_2.disconnect_house(house_2)
                        battery_1.set_connection(house_2)
                        battery_2.set_connection(house_1)
                        return True
        return False


